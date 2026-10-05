# Use the player's position to detonate a single TNT
#   This is done by placing a redstone block first and the TNT on top of it
from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

redstone = 152
TNT = 46

while True:
    p = mc.player.getPos()
    for i in range(5):
        mc.setBlock(p.x, p.y - 2*i - 4, p.z, redstone)
        mc.setBlock(p.x, p.y - 2*i - 3,     p.z, TNT, 1)
    sleep(5)


