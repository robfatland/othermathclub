# This was originally an "orchard with bees somewhere" and you send your drone to go make
#   recordings. The sound you measure is louder with proximity to a hive. I'll reproduce
#   the original markdown followed by 4 versions of Client code.


#######################################


# README.md



# PythonBytes Project In-Depth
## Bees and Drones
### Read the description; and check in with Rob before starting to work on this project
### Use Python 3 at http://replit.com


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/bees#pythonbytes-project-in-depth)


### Overview

Farmers like to see bees (particularly honey bees) in their fields and orchards because the bees help pollinate the plants.
This results in a bigger harvest. 


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/bees/honeybee.png" alt="honey bee" width="350"/>



In this project we imagine that you are a farmer with a large orchard of Baobab trees.
Here to remind you is a picture of the Baobab tree...



<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/bees/baobab.png" alt="baobab" width="350"/>


The orchard is 2000 meters by 2000 meters; plus there is height above the ground in meters.
We can say that the orchard is three-dimensional with coordinates (x, y, z) where x and y
are somewhere between 0 and 2000 and z is somewhere between 0 and 30. 


Now as a farmer you also happen to own a supply of drones, the mechanical kind. These drones
you can send to various locations in your orchard where they can count how many bees are nearby. (They listen 
to the buzzing.)


You goal is to find places where there are lots of bees clustered together. This is called a beehive. 
Once you know
where the hive is you can visit it and cultivate the bees. To learn more about this
you can read [this article](https://en.wikipedia.org/wiki/Swarming_(honey_bee)).


The challenge of this project is to use Python to send your drones out into your orchard to count bees.
Try to find all of the hives but also keep track of how many drones you lose. The best program will win a
special Bee Prize at the end of the year. 


### Details


Somewhere on the internet I have installed a little program that acts like a Python function. You
send it a drone location and it tells you how many bees the drone counted... or it returns 'drone lost'
meaning your drone got stuck in a Baobab tree. We will use coordinates `(x, y, z)` where `x` and `y`
are locations in the orchard between 0 and 2000 meters. `z` will be height above the ground in meters. 
Baobabs can grow as high as 30 meters. 


Now let's ask "how many bees are at (x, y, z)" and see what comes back. Paste this into a
browser window: 


```
--URL-needed-talk-to-Rob--/dronebees?x=12&y=16&z=4
```


Notice that at the very far right it gives what x, y and z are.


I just did this and what I got back looked like a blank web page... until I noticed the number **8** in the upper left corner. 
So apparently there are 8 bees at the coordinates ```(x, y, z) = (12, 16, 4)```. What happens if I hit refresh?
This time I got 5 bees. So the response changes, presumably because the bees are flying around looking for flowers. 
Try changing the values for x, y and z to see what comes up. 


```
# Here is a simple program to test the drones ability to count bees in your orchard
import requests
def bees(x, y, z): 
    return requests.get('https://52t7suregg.execute-api.us-east-1.amazonaws.com/default/' + \
        'dronebees?' + 'x=' + str(x) + '&y=' + str(y) + '&z=' + str(z)).text

# The function bees() returns a string, not an integer, not a float 
myResult = bees(10, 17, 4)
print(myResult)
```


When this runs properly it will either return a number of bees or it will return 'drone lost'. 



The challenge of this project is to think about the logic for locating the bee hives. Since the lost drones
cost some money you would like to be efficient in your search. 



Notice that you can augment your Python program with an incredibly powerful computer: You can use your own brain
to make suggestions. 











#######################################

# Starter code


# This section of code: Keep as-is
import requests, numpy as np, matplotlib.pyplot as plt
def bees(x, y, z): return requests.get('https://52t7suregg.execute-api.us-east-1.amazonaws.com/' + \
        'default/dronebees?' + 'x=' + str(x) + '&y=' + str(y) + '&z=' + str(z)).text


# Test code. Note: This will occasionally give you 'drone lost' as the result
# print(bees(2000., 2000., 50.))



# This is where you modify the code; check with a coach for more details
nStops = 5
dronecounts = np.zeros((nStops,nStops)) 
# result = bees(x, y, z)
# dronecounts[i, j] = float(result)



# This section of code: Keep as-is
fig = plt.figure(figsize=(6, 3.2)); ax = fig.add_subplot(111)
ax.set_title('My Baobab Orchard'); plt.imshow(dronecounts)
fig.savefig('graph.png')





####################################

# Version 2




import requests
import pygame

drones_lost = 0


# This talks to the Internet to find out how many bees are at (x, y, z) ... or 'drone_lost' 
def Bees(x, y, z):
    return requests.get('https://52t7suregg.execute-api.us-east-1.amazonaws.com/default/dronebees?' + \
        'x=' + str(x) + '&y=' + str(y) + '&z=' + str(z)).text

# This creates a little text map of how many bees were found at a grid of locations
def MapBees(x0, y0, z0, r, n):
    global drones_lost
    thisZ = float(z0)
    xa = float(x0 - r)
    xb = float(x0 + r + n)
    dx = 2*r/n
    ya = float(y0 - r)
    yb = float(y0 + r)
    dy = int(2*r/n)
    for i in range(int(n + 1)):
        thisRow = ''
        thisX = xa + i * dx
        for j in range(int(n + 1)):
            thisY = ya + j * dy
            while True:
                b = Bees(thisX,thisY,thisZ)
                if b == 'drone lost': drones_lost = drones_lost + 1
                else: break
            if j == 0: thisRow = str(round(thisX, 1)) + ':  ' + str(round(thisY, 1)) + ' ' + b
            else: thisRow += '   ' + ' ' + str(round(thisY, 1)) + ' ' + b
        print(thisRow)
        print()


# This asks for a new center location (including z) and a radius and a spacing parameter
#   and it goes out and does a square grid of bee counts. It keeps iterating so you can
#   use your evaluation of the data to configure your next search.
def InteractiveLoop():
    while True:
        x0 = float(input('x0: '))
        y0 = float(input('y0: '))
        z0 = float(input('z: '))
        radius = float(input('radius: '))
        n = float(input('n intervals: '))
        dd = drones_lost
        MapBees(x0, y0, z0, radius, n)
        print('\n', drones_lost, ' drones lost total; ', drones_lost - dd, ' this go-round')
        answer = input('quit? ')
        if answer == 'y' or answer == 'yes': break

# This actually starts things off
InteractiveLoop()


#####################################################################


# Version 3


import requests
import pygame

drones_lost = 0


# This talks to the Internet to find out how many bees are at (x, y, z) ... or 'drone_lost' 
def Bees(x, y, z):
    return requests.get('https://52t7suregg.execute-api.us-east-1.amazonaws.com/default/dronebees?' + \
        'x=' + str(x) + '&y=' + str(y) + '&z=' + str(z)).text

# This creates a little text map of how many bees were found at a grid of locations
def MapBees(x0, y0, z0, r, n):
    global drones_lost
    thisZ = float(z0)
    xa = float(x0 - r)
    xb = float(x0 + r + n)
    dx = 2*r/n
    ya = float(y0 - r)
    yb = float(y0 + r)
    dy = int(2*r/n)
    for i in range(int(n + 1)):
        thisRow = ''
        thisX = xa + i * dx
        for j in range(int(n + 1)):
            thisY = ya + j * dy
            while True:
                b = Bees(thisX,thisY,thisZ)
                if b == 'drone lost': drones_lost = drones_lost + 1
                else: break
            if j == 0: thisRow = str(round(thisX, 1)) + ':  ' + str(round(thisY, 1)) + ' ' + b
            else: thisRow += '   ' + ' ' + str(round(thisY, 1)) + ' ' + b
        print(thisRow)
        print()


# This asks for a new center location (including z) and a radius and a spacing parameter
#   and it goes out and does a square grid of bee counts. It keeps iterating so you can
#   use your evaluation of the data to configure your next search.
def InteractiveLoop():
    while True:
        x0 = float(input('x0: '))
        y0 = float(input('y0: '))
        z0 = float(input('z: '))
        radius = float(input('radius: '))
        n = float(input('n intervals: '))
        dd = drones_lost
        MapBees(x0, y0, z0, radius, n)
        print('\n', drones_lost, ' drones lost total; ', drones_lost - dd, ' this go-round')
        answer = input('quit? ')
        if answer == 'y' or answer == 'yes': break

# This actually starts things off
InteractiveLoop()





#########################################


# Final version



# This version runs on the repl.it website.
# Copy/paste this code into a new REPL (make sure in a Python 3 environment) and click the Run button

import requests                                 # this lets the program talk to the internet
import numpy as np                              # this gives you two-dimensional arrays: To represent your orchard
import matplotlib.pyplot as plt                 # this gives you the ability to make a plot of your results

# This function sends your drone to location (x, y, z) and returns the number of bees found there...
#   ...or if you drone got tangled up in the branches of a Baobab tree it returns 'drone lost'
def bees(x, y, z): 
  return requests.get('https://52t7suregg.execute-api.us-east-1.amazonaws.com/' + \
        'default/dronebees?' + 'x=' + str(x) + '&y=' + str(y) + '&z=' + str(z)).text

# Un-comment this next line to check if 'the drones are working ok today'
# print(bees(2000., 2000., 50.))

nStops = 5                                   # This is the number of locations in each dimension (x and y) to visit by drone

dronecounts = np.zeros((nStops,nStops))      # This is the 2-dimensional array representing your orchard

z = 5.                 # The drones measure at z = 5 meters above the ground
lost = 0               # When we begin we have lost zero drones

# Now we simply use two (nested) loops to send out our drones
for i in range(nStops):
  for j in range(nStops):
    x = i*2000./(nStops - 1.)          # This is the x-coordinate for this drone to visit
    y = j*2000./(nStops - 1.)          #   ...and the y-coordinate
    
    while True:                        # This is a do-forever task but it will break once the drone reports back
      bcount = bees(x,y,z)
      if bcount == 'drone lost': lost += 1
      else: break
      
    dronecounts[i, j] = float(bcount)           # We notice that 'bcount' is a string so we must convert it to a float
    print(i, j, 'lost drones =', lost)          # This keeps track of how far along we are (and how many drones lost)


# This section of code creates a plot of the results and displays it as a little image at repl.it
fig = plt.figure(figsize=(6, 3.2))
ax = fig.add_subplot(111)
ax.set_title('My Baobab Orchard')
plt.imshow(dronecounts)
fig.savefig('graph.png')


