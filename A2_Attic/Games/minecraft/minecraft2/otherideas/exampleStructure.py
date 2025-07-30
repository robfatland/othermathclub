# This program builds a tunnel of rings around a moving player in Minecraft

from mcpi.minecraft import Minecraft     # for the Minecraft connector object
from mcpi.vec3 import Vec3               # for 3D vectors
import numpy as np                       # use numpy for math functions
from random import randint               # random integers

mc = Minecraft.create()   # a Minecraft object that connects and talks to the server
p = mc.player.getPos()    # player position
p = p + Vec3(-1000, 0, 0)
p.y = 127
mc.player.setPos(p)

quartz = 155
redstone = 152
TNT = 46
still_water = 9
flowing_water = 8
diamond = 57
flowing_lava = 10
wool = 35
magenta_for_wool = 2
gold = 41
bricks = 45
glass = 95
obsidian = 49
portal = 90

m = [gold, quartz, redstone, diamond, glass, obsidian, portal, wool, TNT, gold]

def cube(x, y, z, s, type):
    for i in range(s):
        for j in range(s):
            for k in range(s): mc.setBlock(x + i, y + j, z + k, type)

p = mc.player.getPos()
x0, y0, z0 = p.x + 15, 100, p.z

for i in range(10): cube(x0 + randint(0,30), y0 + randint(0, 50), z0 + randint(0, 30), randint(20, 40), m[i])

print('ok done building')        

    
