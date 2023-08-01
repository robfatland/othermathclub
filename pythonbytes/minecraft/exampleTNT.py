# Use the player's position to detonate a single TNT
#   This is done by placing a redstone block first and the TNT on top of it
from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

redstone = 152
TNT = 46

while True:
    p = mc.player.getPos()
    mc.setBlock(p.x - 10, p.y - 1, p.z + 10, redstone)
    mc.setBlock(p.x - 10, p.y, p.z + 10, TNT, 1)
    sleep(10)


