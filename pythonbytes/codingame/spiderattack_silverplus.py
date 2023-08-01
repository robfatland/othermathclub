import sys
from random import randint as r
from math import sqrt, cos, sin, radians, atan2

# Notes
# ALLY does not work inside field so keep h0 awaaaaay from field
# only cast ALLY CONTROL on healthy spiders
# turns < 40 h0 should just be hacking for mana
# Technical: Can a SHIELD be cast on myself while I still have one SHIELD point remaining (immune to opp spells)
# This is definitely the first thing to try: 
#    Trail location: Maybe out to the side to clear the path
# review the logic states
# Post-mana wand phase: keep sending them via CONTROL en masse
#    Should be more effective than just following them in

lrh_x, lrh_y = 17630, 9000
diaglen = sqrt(lrh_x**2 + lrh_y**2)
diangle = atan2(lrh_y, lrh_x)
disin   = sin(diangle)
dicos   = cos(diangle)

bx, by = [int(i) for i in input().split()]
ox, oy = lrh_x - bx, lrh_y - by
cx, cy = int(lrh_x/2), int(lrh_y/2)


dir = 1 if not bx else -1
me = 0 if bx == 0 else 1
turn, turn_mod = 0, 6

scsx, scsy = cx + dir*3000, 2000
reachedSCS = False
print('scs: ' + ' ' + str(scsx) + " " + str(scsy), file=sys.stderr, flush=True)
safe_follow = 850

field_radius   = 5000
defog_radius   = 2100
wind_radius    = 1280
wind_move      = 2000
control_radius = 2000
shield_radius  = 2000
shield_turns   = 12
nClosingSteps  = int(5000/400)
faraway        = 2*lrh_x

heroes_per_player = int(input())  # Always 3

def DiagLoc(r):        return (int(bx + dir*r*dicos), int(by + dir*r*disin))
def d2b(x, y):         return sqrt((bx - x)**2 + (by - y)**2)
def d2h(x, y, xh, yh): return sqrt((x-xh)**2+(y-yh)**2)
def d2o(x, y):         return sqrt((x - ox)**2+(y - oy)**2)

def ThreatTurns(x, y, vx, vy):
    '''returns number of turns before a dangerous spider arrives at base'''
    nSteps = 0
    while True:
        x += vx
        y += vy
        nSteps += 1
        if d2b(x, y) <= field_radius: return nSteps + nClosingSteps
        if x < 0 or x > lrh_x or y < 0 or y > lrh_y: return -1

def AllyTurns(x, y, vx, vy):
    '''returns number of turns before a dangerous spider arrives at opponent base'''
    nSteps = 0
    while True:
        x += vx
        y += vy
        nSteps += 1
        if d2o(x, y) <= field_radius:
            return nSteps + nClosingSteps
        if x < 0 or x > lrh_x or y < 0 or y > lrh_y: return -1

# Conditional Complement: Flips coordinates calculated relative to the 
# origin ONLY if base is at (0, 0): For opponent-relative coordinates.
def ConComp(x, y): 
    if me == 0: return (x, y)
    return (lrh_x - x, lrh_y - y)

'''Closest Enemy Within Range'''
def CEWR(E, x, y, r):
    '''presumes E is a list of entities as a tuple (_id, x, y, etcetera)
    x, y is a location and r is a range of interest. Returns a fourple pointing
    at the nearest exemplar from all of E: (B, Ex, Ey, Ei). B is a bool for d(E to (x,y)) < r'''
    if len(E) == 0: return (False, -1, -1, -1, -1)
    closest_r = faraway
    closest_x = -1
    closest_y = -1
    closest_i = -1
    for i in range(len(E)):
        this_range = d2h(E[i][1], E[i][2], x, y)
        if this_range < closest_r: 
            closest_r = this_range
            closest_x, closest_y = E[i][1], E[i][2]
            closest_i = i
    if closest_r < r: return (True,  closest_x, closest_y, closest_i, closest_r)
    return (False, closest_x, closest_y, closest_i, closest_r)

def H1Model(t):
    '''model for Hero 1 to gradually return to base'''
    farthest = 4000
    nearest = 2000
    if t < 10: return(DiagLoc(farthest))
    if t > 60: return(DiagLoc(nearest))
    model_radius = farthest - (t - 10)*(farthest-nearest)/(80-10)
    return(DiagLoc(model_radius))

# Simplified commands with appended message optional
def M(x, y, m=''):     print("MOVE " + str(int(x)) + " " + str(int(y)) + " " + m)
def C(id, x, y, m=''): print("SPELL CONTROL " + str(id) + " " + str(int(x)) + " " + str(int(y)) + " " + m)
def W(x, y, m=''):     print("SPELL WIND " + str(int(x)) + " " + str(int(y)) + " " + m)
def S(id, m=''):       print("SPELL SHIELD " + str(id) + " " + m)
def T(m=''):           print("WAIT " + m)

def sem(m): print(m, file=sys.stderr, flush=True)

def Trail(entity, safe_distance):
    x, y = entity[1], entity[2]
    vx, vy = entity[3], entity[4]
    speed = sqrt(vx**2 + vy**2)
    x1, y1 = x + vx, y + vy
    vangle = atan2(vy, vx)
    vangle_plus_90 = vangle + radians(90)
    vx_rot = cos(vangle_plus_90)
    vy_rot = sin(vangle_plus_90)

    if speed == 0.: print("Zero Speed ALERT!!!", file=sys.stderr, flush=True)
    lateral_x = vx_rot*safe_distance   # lateral delta (perp to v) scaled to safe distance behind
    lateral_y = vy_rot*safe_distance
    tx, ty = int(x1 + lateral_x), int(y1 + lateral_y)
    if tx < 0: tx = 0
    if tx > ox: tx = ox
    if ty < 0: ty = 0
    if ty > oy: tx = oy    
    M(tx, ty, 'h0 M Trail ' + str(entity[0])) 
    return True


while True:
    turn = turn + 1
    
    mana2, health2 = [], []
    for i in range(2):  # two players
        health, mana = [int(j) for j in input().split()]
        mana2.append(mana)
        health2.append(health)

    my_mana = mana2[me]

    entity_count = int(input())  # Amount of heros and monsters you can see
    if   entity_count < 3:  print('   uh oh...', file=sys.stderr, flush=True)
    elif entity_count == 3: print('   nothing to see but me...', file=sys.stderr, flush=True)
    
    enemies   = []    # all monsters
    threats   = []    #   ...monsters that will arrive at my base
    allies    = []    #   ...monsters that will arrive at opponent's base
    heroes    = []    # me x 3, indices 0 1 2
    opponents = []    # opponent x 3, indices 3 4 5

    for i in range(entity_count):
        # _id: Unique; _type: 0=monst, 1=me, 2=opp; x / vx: pos / move per turn
        # shield_life: Count down until shield spell fades
        # is_controlled: 1 when this entity is under a control spell
        # health: Remaining; near_base: bool monster on field
        # threat_for dest: 0 none / 1 me / 2 opp
        _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = \
            [int(j) for j in input().split()]

        if _id == 0: h0x, h0y = x, y
        
        d2h0 = d2h(x, y, h0x, h0y) 

        # build enemies, heroes, opponents lists: Always indices 0 ... 10; threats and allies have 11
        if _type == 0:
            enemies.append((_id, x, y, vx, vy, threat_for, shield_life, \
                            is_controlled, health, near_base, d2h0))  
            outcome = ThreatTurns(x, y, vx, vy)
            if outcome > -1: 
                threats.append((_id, x, y, vx, vy, threat_for, shield_life, \
                                is_controlled, health, near_base, d2h0, outcome))
            outcome = AllyTurns(x, y, vx, vy)
            if outcome > -1: 
                print('ally: ' + str(_id) + ' ' + str(x) + ' ' + str(y) + ' ' + \
                                 str(vx) + ' ' + str(vy), file=sys.stderr, flush=True)
                allies.append((_id, x, y, vx, vy, threat_for, shield_life, \
                                            is_controlled, health, near_base, d2h0, outcome))
        elif _type == 1: 
            heroes.append((_id, x, y, vx, vy, threat_for, shield_life, \
                                is_controlled, health, near_base, 0))
        elif _type == 2:
            opponents.append((_id, x, y, vx, vy, threat_for, shield_life, \
                                is_controlled, health, near_base, d2h0))

    # sorted by distance (in turns) from my / opp base
    threats.sort(key = lambda x: x[10])
    allies.sort(key = lambda x: x[10])

    # CEWR in global-range relationship to hero 0
    e = CEWR(enemies, h0x, h0y, faraway)             # result: bool exist, its x, y, index, range
    a = CEWR(allies, h0x, h0y, faraway)   

   
    ###################    
    # HERO 0 at h0x, h0y        e[]/a[] indices are bool, x, y, index, range to hero 0
    ###################
    if h0x == scsx and h0y == scsy: reachedSCS = True
    if turn < 40:                                                                     # turn < 40 
        if not reachedSCS:                                                            #     !scs
            M(scsx, scsy, "h0 MOVE to scs in M phase")
        else:                                                                         #     scs
            if e[0]:                                                                  #         closest enemy exists
                ce = enemies[e[3]]
                ce_x1 = ce[1] + ce[3]
                ce_y1 = ce[2] + ce[4]
                M(ce_x1, ce_y1, "h0 MOVE toward closest enemy projected in M phase")
            else:                                                                     #         !closest enemy exists
                M(h0x + r(100,400), h0y + r(100,400), "h0 MOVE fidget in M phase")
    else:                                                                             # turn >= 40
        if not len(allies):                                                           # !ally
            if not len(enemies):                                                      #       !enemy
                if not reachedSCS:                                                    #             !scs
                    M(scsx, scsy, "h0 MOVE to scs")
                else:                                                                 #             scs
                    T("h0 WAIT at scs")
            else:                                                                     #        enemy 
                if e[4] > 2000:                                                       #             distal
                    Trail(enemies[e[3]], safe_follow)
                else:                                                                 #             proximal
                    if my_mana < 10:                                                  #                   !M
                        Trail(enemies[e[3]], safe_follow)
                    else:                                                             #                   M 
                        sem("control 0 " + str(e[3]) + ' ' + str(enemies[e[3]][0]))
                        C(enemies[e[3]][0], ox, oy, "h0 CONTROL enemy to ally")
        else:                                                                         # ally
            aPrime = allies[a[3]]
            if a[4] < safe_follow:                                                    #     h0 too close
                Trail(aPrime, safe_follow)
            elif a[4] > 1500:                                                         #     h0 too far  
                Trail(aPrime, safe_follow)
            else:                                                                     #     h0 good distance
                if not aPrime[6]:                                                     #          ally !shield
                    if my_mana < 10:                                                  #              !M
                        Trail(aPrime, safe_follow)
                    else:                                                             #              M
                        S(aPrime[0], "h0 shield aPrime")
                else:                                                                 #          ally shield
                    if not len(opponents):                                            #              !opp
                        Trail(aPrime, safe_follow)
                    else:                                                             #              opp
                        owrta = CEWR(opponents, aPrime[1], aPrime[2], 2000)
                        if not owrta[0]:                                              #                  opp ally-distal
                            owrth0 = CEWR(opponents, h0x, h0y, 2000)
                            if not owrth0[0]:                                         #                     opp h0-distal 
                                Trail(aPrime, safe_follow)
                            else:                                                     #                     opp h0-proximal
                                if not heroes[0][6]:                                  #                          h0 !shield
                                    if my_mana < 10:                                  #                               !M
                                        Trail(aPrime, safe_follow)
                                    else:                                             #                               M
                                        S(0, 'h0 SHIELD self') 
                                else:                                                 #                          h0 shield
                                    Trail(aPrime, safe_follow)            
                        else:                                                         #                  opp ally-proximal
                            owrth0 = CEWR(opponents, h0x, h0y, 2000)            
                            if not owrth0[0]:                                         #                      opp h0-distal  
                                Trail(aPrime, safe_follow)
                            else:                                                     #                      opp h0-proximal
                                if not heroes[0][6]:                                  #                          h0 !shield
                                    if my_mana < 10:                                  #                              h0 !M
                                        Trail(aPrime, safe_follow)
                                    else:                                             #                              h0 M 
                                        S(0, 'h0 SHIELD self')
                                else:                                                 #                          h0 shield
                                    if my_mana < 10:                                  #                              !M
                                        Trail(aPrime, safe_follow)
                                    else:                                             #                              M
                                        C(opponents[owrta[3]][0], bx, by, \
                                              'h0 CONTROL opp away from ally')

    ###################
    # HERO 1
    ###################

    # hero 1 harvests mana and gradually returns to fields, arriving at turn 80
    h1x, h1y = heroes[1][1], heroes[1][2]
    h1d = CEWR(enemies, h1x, h1y, 2000)       # hero 1 Closest Enemy Within Range data
    if h1d[0]: M(h1d[1], h1d[2], "h1 enemy")
    else:      mx, my = H1Model(turn); M(mx, my, "h1 model")

    ###################
    # HERO 2
    ###################

    h2x, h2y = heroes[2][1], heroes[2][2]
    h2d = CEWR(threats, h2x, h2y, 2000)       # hero 2 Closest (Threat) Within Range data
    if h2d[0]:
        ti = h2d[3]
        tx, ty = threats[ti][1], threats[ti][2]
        M(tx, ty, "h2 threat")
    else: 
        h2x, h2y = DiagLoc(2000)
        M(h2x, h2y, "h2 diagonal")
