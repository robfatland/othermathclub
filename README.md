[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robfatland/othermathclub/HEAD)


# the other math club

Question: Have you ever read a book about a *seemingly* ordinary world
when suddenly the rules change? 
Have you ever felt a moment of *imbalance* as you turn the pages?
Have you teetered on the edge of a rabbit hole and then tumbled down 
in slow motion past cupboards and jars of marmalade?
Have you ever found yourself in a new world inside a book?  And by this 
I mean a world that is built from echoes of the 
ordinary together with something extraordinary and amazing...
well I must admit I have; so I will carry on assuming you have as well.


Which book did you find?
Was it about a girl who found it curious that a rabbit passing by muttered to itself? 
Perhaps the book concerned
climbing into a wardrobe. Perhaps it was a book about a boy who learns he is actually a wizard. 
Perhaps it was a book with a live dragon waiting at the end, asleep on a mountain of gold.


This book is related to -- is inspired by -- such books.
So I begin by explaining two important differences between those books and this one.
First, when you set down
those other books (because it is time to go to sleep or much worse because you have finished
the last page) you know you are returning to the real and the ordinary world where rabbits
do not check their watches and trolls do not turn to stone in the morning sunshine. 
This book, on the other hand, is not like that. Everything in this book is real, 
with actual reasons for being so. This book seeks after things *extraordinary*
but it insists on realness. This brings me to the second difference. 


When we read about an extraordinary world we are presented with certain facts that are 
simply so. The author says: 'There are trolls here.' There it is. The agreed-upon rule is: 
They say there are trolls so we accept that as fact and keep reading.
In *this* book the difference is: Because the extraordinary claims to be real, 
you have the option to decide if you agree. You choose. 


If you have read this far: You are a good candidate for reading more of this book.
If you have not read this far: Maybe someone who has read this book will tell you
about it. 


If you have a bit of blank paper and a pencil on hand: You are even more so a good 
candidate for reading more of this book. If you pick up the pencil and draw a
square on the paper... and draw another square overlapping it, offset up and to the right
a bit, and if you connect the nearest four corners of the two squares with four
diagonal lines: You have a cube to stand on, you are on your way. 


Here is the deal this book offers: I will do my best 
to convey the extraordinary, and you do your best to think about it using
your imagination and a pencil and paper... but you must think **slowly**. 
What does it mean to think slowly? A chap named Daniel Kahneman
describes thinking slowly in terms of how our brain deals with new information. 
He says that the new information starts out by making no sense to us. We could imagine it is
kind of *blurry*. So we enter a slow-thinking trance where the new thing gradually gradually
comes into focus.  It becomes a part of our understanding. Something interesting 
happens in this process: If you focus your mind, slowly, on
something that is extraordinary... and you keep focusing
on it... and gradually it comes into focus... and you come to understand it... 
then **you** have become *more extraordinary*. 


There is my secret. This is a book about becoming more extraordinary.
You are extraordinary to begin with, for so many reasons I could spend
hours and hours telling you. But the wonderful news about this world is
that there is always room to discover more.
Understand that *you* will be doing all the work. I am simply 
acting as a *messenger* bringing you the invitation. I hold the door open, 
you do the work of passing through. 


Let us begin with a story about a Fishing Kid. 


## The Fishing Kid


Once upon a time there was a kid who wished to go fishing... but she did not 
have a fishing pole. She did manage to find a five foot steel pipe and (as
she did not realize fishing poles are supposed to be very bendy) she decided 
the metal pipe would be her fishing pole. 


She gathered up some string and made a hook from a 
paper clip and grabbed a bag of cheese puffs to use as bait. She put five dollars
in her pocket from her savings and she walked to the nearby bus stop to wait for
the bus. When it arrived she paid her bus fare (one dollar) and rode the bus
for 45 minutes to a bridge across a river. The bus driver did not seem to be 
paying her any attention... but he looked rather surprised at the pipe 
when she left the bus. 


As she walked towards the bridge she passed a post office. A sign out front 
advertised cubical moving boxes, so many feet on a side. A small one foot cubical 
moving box cost $1, a two foot box cost $2, and so on up to five feet. 


She continued on and made her way down to the banks of the river that flowed under
the bridge. (It was called the D'enigmes River.)  She began fishing, a cheese puff
skewered on the paper clip hook, attached to the metal pole by the string. 


As you might guess, not a lot happened. Time passed. Minutes stretched to hours and
never a bite from a fish, not even a nibble... and the cheese puffs would become
soggy and fall off the hook and drift away. She decided to give up; and she 
returned to the bus stop near the river slightly disappointed. 


The bus pulled up but this time the driver was paying attention. As the girl began
to board the bus driver said, 'No no no, I'm sorry but you may not bring anything
on the bus longer than three feet. That metal pole is certainly five feet long.' 


Now she is in a dilemma. She does not want to abandon her fishing pole... but the 
bus is her only way home. What should she do?


link to page 2 here


## Fine print

- Some ideas require repetition; so computers




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
