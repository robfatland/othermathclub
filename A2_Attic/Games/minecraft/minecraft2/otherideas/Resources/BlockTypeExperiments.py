from mcpi.minecraft import Minecraft
import numpy as np
import random as r
import time
import kilroy

pi = np.pi
def d2r(d): return pi*d/180.0
def r2d(r): return 180.0*r/pi


quartz = 155
air = 0
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


def msg(msg):
    mc.postToChat(msg)
    print(msg)

mc = Minecraft.create()
xPos, yPos, zPos = 12301, 78, 964             
mc.player.setPos(xPos, yPos, zPos)

pos=mc.player.getPos()
tessPos = mc.player.getPos()
spherePos = mc.player.getPos()
waterPos = mc.player.getPos()
stackPos = mc.player.getPos()

##print(pos, tessPos, spherePos,waterPos)

tessPos.x += 20
tessPos.y += 30
tessPos.z += 0
spherePos.x += 30
spherePos.y += 50
spherePos.z += -10
waterPos.x += 7
waterPos.y += 3
waterPos.z += 0
stackPos.x += 20
stackPos.y += 4
stackPos.z += 0

print(pos, tessPos, spherePos, waterPos)
msg("end init")

msg("block of water, tesseract, sphere")

##mc.setBlock(waterPos.x + 7, waterPos.y + 3, waterPos.z, still_water)
kilroy.TesseractPortal(mc, tessPos, [31, 31, 31, 15, 15, 15], air, air)
##kilroy.SparseSphereShell(mc, spherePos, 67, 2, air)

##msg("60 second pause starts now")


##time.sleep(30)
##
##msg("time to clean up")
##
##mc.setBlock(waterPos.x + 7, waterPos.y + 3, waterPos.z, air)
##kilroy.Tesseract(mc, tessPos, [31, 31, 31, 15, 15, 15], air)
##kilroy.SparseSphereShell(mc, spherePos, 67, 2, air)
##
##msg("experimental block stack")
##
##mc.setBlock(stackPos.x, stackPos.y+0, stackPos.z, quartz)
##mc.setBlock(stackPos.x, stackPos.y+1, stackPos.z, air)
##mc.setBlock(stackPos.x, stackPos.y+2, stackPos.z, redstone)
##mc.setBlock(stackPos.x, stackPos.y+3, stackPos.z, wool, 7)
##mc.setBlock(stackPos.x, stackPos.y+4, stackPos.z, TNT, 1)
##mc.setBlock(stackPos.x, stackPos.y+5, stackPos.z, diamond)
##mc.setBlock(stackPos.x, stackPos.y+6, stackPos.z, wool, 3)
##mc.setBlock(stackPos.x, stackPos.y+7, stackPos.z, gold)
##mc.setBlock(stackPos.x, stackPos.y+8, stackPos.z, bricks)
##mc.setBlock(stackPos.x, stackPos.y+9, stackPos.z, glass)
##
##mc.postToChat("done setblocks, waiting 10 secs")
##print("done setblocks, waiting 10 secs")
##time.sleep(10)
##
##for j in range(10):
##    block = mc.getBlockWithData(stackPos.x, stackPos.y + j, stackPos.z)
##    print(pos.y + j, block.id, block.data)

##msg("done!!!!")
   
# key idea: pos = mc.player.getPos() gets us
# pos.x (east-west)
# pos.y (vertical)
# pos.z (north-south)
# ...and that is *all* in fact...


# block types:
#   0      air
# 155      quartz
# 152      redstone
#  12      sand
#  46      TNT
#  10      flowing lava
#  35      wool
#      2   magenta qualifier on wool
    
# Aidan challenge
##msg('Da Boom for Aidan')
##xPos, yPos, zPos = 11961, 68,1031
##mc.player.setPos(xPos,yPos,zPos)
##cuboidPos = mc.player.getPos()
##xwid = 32
##ywid = 32
##zwid = 32
##cuboidPos.x -= xwid/2
##cuboidPos.y += ywid/2 + 10
##cuboidPos.z += 0

##for i in range(int(cuboidPos.x), int(cuboidPos.x + xwid)):
##    for j in range(int(cuboidPos.y), int(cuboidPos.y + ywid)):
##        for k in range(int(cuboidPos.z), int(cuboidPos.z + zwid)):
##            mc.setBlock(i, j, k, obsidian) 
##
##airPos = mc.player.getPos()
##xwidAir = 30
##ywidAir = 30
##zwidAir = 30
##airPos.x -= xwid/2 - 1
##airPos.y += ywid/2 + 10 + 1
##airPos.z += 1
##
##for i in range(int(airPos.x), int(airPos.x + xwidAir)):
##    for j in range(int(airPos.y), int(airPos.y + ywidAir)):
##        for k in range(int(airPos.z), int(airPos.z + zwidAir)):
##            mc.setBlock(i, j, k, air)



##mc.setBlock(xPos - 3, yPos + 4, zPos + 3, portal)
##
##mc.setBlock(xPos - 5, yPos + 4, zPos + 5, portal)
##
##mc.setBlock(xPos - 3, yPos + 4, zPos + 5, portal)
##
##mc.player.setPos(1, 100, 1)




