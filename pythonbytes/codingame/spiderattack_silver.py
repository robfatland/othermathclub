import sys
import math
from random import randint as r
from math import sqrt

# Notes On This Game So Far: To Read Upon Return
# 
# Fog of war gives an information radius of about 2100 pixels
#   Determines inbound enemy information (even though others are visible)
#   When the enemy list is occupied: Better just go kill them
#   When not: Try and disperse information disks to maximize information
#
# Fields have a radius of 5000 centered on bases at opposite corners
#   Once a spider is inside the field it turns to go towards the base
#   Fog of war does not affect fields; have complete information
#   Mana from outside of fields is 'wild mana' and it counts towards tie breaks
#
# Health starts at 3; spider arriving at base drops health by 1
#   Current algorithm concentrates on move/hack, all 3 heroes, ranks about 700
#
# Spider information vx, vy is how far in one turn, couple hundred pixels
#   The Propagate() function improves over the native threat_for
#       It returns n turns before this spider inside 'fields'
#       BUT this information is not currently in use
#       ALSO it is inefficient code (checks every turn)
#           EXCEPT when the opponents starts re-vectoring spiders using spells
#
# Spells are now available but not in use by this code
#     Spells are clearly necessary to win this level
#     Boss 3 uses CONTROL spell but not WIND (more useful?)
#
# Ideally move/fight/spell with only two fighters to keep base clear...
#     And then hero 3 operates distal with two purposes
#         1. harvest mana for spells (10 per)
#             (this implies moving to hit non-threat spiders)
#         2. push spiders towards opponents base using spells
#
# Suggested approach
# Put one hero out to pasture to just kill any bugs it sees
# Heroes 2 and 3 work the defense mechanically
# Then add spells
# It seems that multiple spiders in sword range take independent damage
# It seems that preemptively killing threats earlier (not JIT) enables more 'wild mana'
#
# End notes ---------------------------- 
#
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# base_x: The corner of the map representing your base
# base is either (0, 0) or (17630, 9000), revector radius 5000
base_x, base_y = [int(i) for i in input().split()]
ebase_x, ebase_y = 17630 - base_x, 9000 - base_y

# Debug: print(msg, file=sys.stderr, flush=True)

if base_x == 0: dir_factor = 1
else:           dir_factor = -1

# dispersed default, index [1] will be the center point
defog_radius = 2100
post_a = 5100
post_b = defog_radius
post_c = int((math.sqrt(2)/2)*sqrt(post_a**2 + post_b**2))

px0 = str(int(base_x + dir_factor*post_a))
px1 = str(int(base_x + dir_factor*post_b))
px2 = str(int(base_x + dir_factor*post_c))

py0 = str(int(base_y + dir_factor*post_b))
py1 = str(int(base_y + dir_factor*post_a))
py2 = str(int(base_y + dir_factor*post_c))

sddx = [px0, px1, px2]
sddy = [py0, py1, py2]

heroes_per_player = int(input())  # Always 3
hpp = heroes_per_player


center_x = 17630/2
center_y = 9000/2
respond_range = 1000
field_radius = 5000

def d2b(x, y): return sqrt((base_x - x)**2 + (base_y - y)**2)
def d2h(x, y, xh, yh): return sqrt((x-xh)**2+(y-yh)**2)
def Propagate(x, y, vx, vy):
    nSteps = 0
    while True:
        x += vx
        y += vy
        nSteps += 1
        if d2b(x, y) < field_radius: return nSteps
        if x < 0 or x > 17630 or y < 0 or y > 9000: return -1

# Conditional Complement: Reverses coordinates calculated relative to the 
# origin (i.e. to focus on Opponent's base) only when our base is at (0, 0)
def ConCom(x, y): 
    if base_x == 0: return (x, y)
    return (17630 - x, 9000 - y)

'''use this to do nothing temporarily while developing'''
def PrintWait(): print("WAIT"); print("WAIT"); print("WAIT")

# game loop
while True:
    for i in range(2):
        # health: Each player's base health
        # mana: Ignore in the first league; Spend ten mana to cast a spell
        health, mana = [int(j) for j in input().split()]
    entity_count = int(input())  # Amount of heros and monsters you can see

    min_threat_range = d2b(center_x, center_y)
    threat_index, threat_x, threat_y = -1, center_x, center_y
    
    enemies = []
    heroes = []

    for i in range(entity_count):
        # _id: Unique identifier
        # _type: 0=monster, 1=your hero, 2=opponent hero
        # x: Position of this entity
        # shield_life: Ignore for this league; Count down until shield spell fades
        # is_controlled: Ignore for this league; Equals 1 when this entity is under a control spell
        # health: Remaining health of this monster
        # vx: Trajectory of this monster
        # near_base: 0=monster with no target yet, 1=monster targeting a base
        # threat_for: Given this monster's trajectory, is it a threat to 1=your base, 2=your opponent's base, 0=neither
        _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = [int(j) for j in input().split()]
        
        # This here is wildly successful but can't beat Boss 3
        # if _type == 0 and d2b(x, y) < min_threat_range: min_threat_range, threat_x, threat_y = d2b(x, y), x, y

        # This here is a targeted debug section that led to the discovery of how fog of war works...
        # if _id == 9: print(str(_id) + ' ' + etcetera, file=sys.stderr, flush=True)

        if _type == 0 and threat_for == 1: 
            outcome = Propagate(x, y, vx, vy)
            if outcome > 0: 
                enemies.append((_id, x, y, vx, vy, outcome, threat_for))
            else:
                print('Prop() disagrees with threat_for', file=sys.stderr, flush=True)

        elif _type == 1: heroes.append((_id, x, y, vx, vy))

    # sorted by distance from base-circle
    enemies.sort(key = lambda x: x[5])
    
    lenen = len(enemies)
    if lenen:
        on_fields = d2b(heroes[0][1], heroes[0][2]) < field_radius or \
                    d2b(heroes[1][1], heroes[1][2]) < field_radius or \
                    d2b(heroes[2][1], heroes[2][2]) < field_radius
        if on_fields:
            e0x, e0y = enemies[0][1], enemies[0][2]
            for i in range(3):
                hx, hy = heroes[i][1], heroes[i][2]
                if d2h(e0x, e0y, hx, hy) < 1280: print("SPELL WIND " + str(ebase_x) + " " + str(ebase_y))
                else:                            print("MOVE " + str(e0x) + " " + str(e0y))

        else:
            e0x = str(int(enemies[0][1]))
            e0y = str(int(enemies[0][2]))
            if lenen == 1:
                print("MOVE " + e0x + " " + e0y) 
                print("MOVE " + e0x + " " + e0y) 
                print("MOVE " + e0x + " " + e0y)
            else: 
                e1x = str(int(enemies[1][1]))
                e1y = str(int(enemies[1][2]))
                print("MOVE " + e0x + " " + e0y) 
                print("MOVE " + e0x + " " + e0y) 
                print("MOVE " + e1x + " " + e1y)


    else: 
        for i in range(hpp): print("MOVE " + sddx[i] + " " + sddy[i])

        # In the first league: MOVE <x> <y> | WAIT; In later leagues: | SPELL <spellParams>;
        # print("WAIT")
