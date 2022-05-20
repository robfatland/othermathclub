[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robfatland/othermathclub/HEAD)


# the other math club

Have you ever read a book about the seemingly ordinary world? Have you ever felt that moment of
imbalance as you teetered on the edge of the rabbit hole?  Before you fell forward and down; 
and found yourself in a world?  That new world that contained echoes of the ordinary one...
but was full of the amazing, the new and the extraordinary? 


Maybe it was a book about a girl named Alice. Maybe it was a book about the Pevensee 
children climbing into a wardrobe that became a forest when you push past the first layer
of coats. Maybe it was a book about a boy who is told he is actually a wizard. Perhaps
it is a book with a live dragon waiting for you at the end.


This book is such a book, with two important differences. First, when you set down
those other books because it is time to go to sleep or much worse because you have finished
the last page, you know you are returning to the real and the ordinary world where rabbits
do not check their watches and trolls do not turn to stone in the morning sunshine. 
This book is not like that. Everything in this book is real, with actual reasons for 
being so, despite it being extraordinary. And this brings me to 
the second difference. 


When you read about an extraordinary world you are presented with certain facts that are 
simply so. If you are presented with facts in a story you know the rule: You simply accept
them as how things are, and you continue from there. Because the extraordinary things 
in this book are true, you can convince yourself if you so choose. 


If you have read this far: You are a good candidate for reading more in this book. 
If you have a fairly blank piece of paper and a pencil handy: You are a good 
candidate for reading more in this book. If you now pick up the pencil and draw a
square on the paper... and another square overlapping it offset up and to the right
a bit, and if you connect the nearest corners of the two squares with lines to
produce a cube: You are already on your way. The deal is this: I will do my best 
to convey the extraordinary world, and you do your best to think about it using
that pencil... but you must think **slowly**. What does this mean? Daniel Kahneman
describes it in terms of what our brain does the first time we encounter something
new. We enter a sort of trance where the new thing slowly slowly slowly comes into
focus, becomes a part of our understanding. So notice an interesting thing: If I 
tell you about something extraordinary... and you slow your thinking down to focus
upon it... and gradually you come to understand it... then **you** have become
*more extraordinary*. 


So there is my secret. This is a book about you become extraordinarier in this
ordinary world. But you will be doing all of the work. I am simply a messenger
bringing you the invitation. I hold the door, you pass through it. And with 
that let us begin with the story of the Fishing Kid. 


## The Fishing Kid


Once upon a time there was a kid who wished to go fishing... but she did not 
have a fishing pole. She did manage to find a five foot metal pipe and (as
she did not realize fishing poles are supposed to be very bendy) she decided 
the metal pipe would do. She gathered up some string and made a hook from a 
paper clip and grabbed a bag of cheetos to use as bait. And she put ten dollars
in her pocket from her savings and walked to the nearest bus stop to wait for
the bus. When it arrived she paid her bus fare (one dollar) and rode the bus
for 45 minutes to a bridge. The bus driver did not really pay any attention 
to her the whole time. 


Standing there on the bridge she noticed a post office on the other side of the
street; but she thought nothing of it. Of course after she made her way down to the banks of the river that flowed under
the bridge, she began fishing rather hopefully with a cheetoh for bait and her 
string for a line and her metal pole that was not at all flexible as her fishing
rod. But minutes stretched to hours with never a bite even a nibble... and the
cheetos would get soggy and fall off the hook and drift away. After a time she
decided it was no good. 

### Sometimes it can be interested to have a computer check out an idea

This presentation of mathematics also includes some Python code. If Python is not 
your thing: You can just ignore it.



### Code fragment

For historical reasons I am preserving a little bit of Python code here. It just loads 
images for illustration purposes. 


```
def Show(folder, filename, width, height):
    """
    import an image from the repo images/folders for dispaly in a Python cell
    """
    import requests, shutil
    from PIL import Image
    fullpath = 'https://raw.githubusercontent.com/robfatland/othermathclub/master/images/' + folder + '/' + filename
    a = requests.get(fullpath, stream = True)
    outf = './sometmp.png'
    if a.status_code == 200:
        with open(outf, 'wb') as f:
            a.raw.decode_content = True
            shutil.copyfileobj(a.raw, f)
    return Image.open(outf).resize((width,height),Image.ANTIALIAS)
```

### Another code fragment


I think this has to do with the planet + moons spaceship escape problem...


```
import turtle

from random import random
from turtle import Turtle
from math import sqrt
from math import cos
from math import sin
from math import atan2
from math import pi

def d(a, b): return sqrt((a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1]))

def SetPlanets():
    global p, n, mass, radius, pSpace
    for i in range(n):
        if i == 0: p.append((0, 0, mass[i], radius[i]))   # place Jupiter at the origin
        else:                                             # four moons
            tryAgain = True
            while tryAgain:
                tryAgain = False
                xm, ym = -pSpace + 2*pSpace*random(), -pSpace + 2*pSpace*random()
                for j in range(i):
                    if d((xm, ym), (p[j][0], p[j][1])) < p[j][3] + radius[i]: tryAgain = True
            p.append((xm, ym, mass[i], radius[i]))

def DrawPlanets():
    for i in range(n): 
        s.up()
        s.setpos(p[i][0], p[i][1]-p[i][3])  # shift down by radius; with heading 0 places the center as desired
        s.down()
        s.circle(p[i][2]*rFactor)

s=Turtle(); s.speed(0); s.down(); s.dot(3); s.up()


# Acceleration multiplier: Determines how intense the gravity is
#   Make this negative for anti-gravity!!!
aFactor = 2.

pSpace = 160.
time = 300
subtime = 20
n = 5
mass = [10., 0.3, 4.1, 2.6, 3.3]
rFactor = 2
radius = [rFactor*i for i in mass]
p = []
SetPlanets()
DrawPlanets()
s.hideturtle()

b=Turtle(); b.speed(0); b.up(); b.color('red')
y0 = 20.
yI = 20.
ny = 4
for i in range(ny):
    x, y = -200., y0 + i*yI
    vx, vy = 0.5/float(subtime), 0.0/float(subtime)
    b.setpos(x,y)
    b.down()
    for t in range(time):
        for subt in range(subtime):
            for j in range(n):
                distance = d((x, y), (p[j][0],p[j][1]))
                accel = aFactor*p[j][2]/(distance*distance)/float(subtime)
                angle = pi*b.towards(p[j][0], p[j][1])/180.
                vx += accel*cos(angle)
                vy += accel*sin(angle)
            x = x + vx
            y = y + vy
        b.setheading((180./pi)*atan2(vy, vx))
        b.setpos(x, y)
        b.dot(1)
    b.up()       
```
