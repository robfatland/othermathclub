# This program builds a tunnel of rings around a moving player in Minecraft

from mcpi.minecraft import Minecraft     # for the Minecraft connector object
from mcpi.vec3 import Vec3               # for 3D vectors
import numpy as np                       # use numpy for math functions
import time                              # for a little timer

mc = Minecraft.create()   # a Minecraft object that connects and talks to the server
p = mc.player.getPos()    # player position

polling_interval = 0.50   # seconds where 0.5 is pretty sparse, 0.05 fairly dense

maxRadius = 6              # max tunnel radius

gold, air = 41, 0    # a couple of brick types (but flowers tend to fall out of the sky)
counter = 0

while True:  # simple form of a loop; will never end
    
    # time.sleep(polling_interval)    # wait a fraction of a second
    counter += 1                    # increase the while-loop counter
    print(counter)
    # if counter > 200: break         # fall out of the program after 200 loops
    
    p2 = mc.player.getPos()                        # the current player position
    v = p2 - p                                     # the vector from previous to current
    mag_v = np.sqrt(v.x*v.x + v.y*v.y + v.z*v.z)   # the distance moved since last position fix

    if mag_v > 0.5:    # only if the player has moved since last position fix

        for ad in range(1, 7):
            ahead_distance = float(ad)
            v.x *= ahead_distance/mag_v          # (v.x, v.y, v.z) is the velocity vector
            v.y *= ahead_distance/mag_v          #    ...it points in the direction the player is moving
            v.z *= ahead_distance/mag_v          #    ...and so is the guide for tunnel-building direction

            xzHeading = -np.arctan2(v.x, v.z)    # azimuth heading in the xz plane
            cc = p2 + Vec3(v.x, v.y, v.z)        # 'circle center' = cc

            mc.setBlock(cc.x, cc.y, cc.z, air)
            for r in range(2, maxRadius + 1):
                fr = float(r)
                for thetaIndex in range(int(6.4*fr)):                                 # ring index: going around a circle
                    theta = float(thetaIndex)*2.*np.pi/64.                   # get an angle from this (radians)
                    dy, dx = fr*np.sin(theta), fr*np.cos(theta)      # two coordinates of circle
                    dxx, dxz = np.cos(xzHeading)*dx, np.sin(xzHeading)*dx    # xz-plane coordinates
                    mc.setBlock(cc.x + dxx, cc.y + dy, cc.z + dxz, air)     # set a block in the ring

    p = p2    # loop is done so reset the 'old' position p to be the current position

print('ok done tunnel building')        

    
