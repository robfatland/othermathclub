from mcpi.minecraft import Minecraft
from random import randint

mc = Minecraft.create()
p = mc.player.getPos()

for j in range(90, 180, 6):
    for i in range(0, 32, 4):
        for k in range(0, 32, 4):
            (dx, dy, dz, block) = (randint(-2, 2), randint(-3, 3), randint(-2,2), randint(0, 255))
            mc.setBlock(p.x - i + dx, j + dy, p.z + k + dz, block)
