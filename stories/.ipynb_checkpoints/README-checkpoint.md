# PythonBytes Project In-Depth


<img src="https://github.com/robfatland/othermathclub/blob/master/pythonbytes/projects/fractals-I/wharf.png" alt="drawing" width="400"/>


These project ideas require you to have a Python environment where you can do some serious work. You can
work at cswonders.com if you like; or come and see the coaches about some other ideas.


Also before we begin: There is a lot here to read and think about. However if you would like to get started on 
the projects (there are three here) just skip down to where it says **Project 1** or **Project 2** or **Project 3**.


### Overview


*'Chaos'* means crazy randomness and disorder in English; but in mathematics it has a more specific meaning. Chaos
in math is based on the idea of a *dynamical system*. So what does this mean? A system for our purposes is an
imaginative model; like something you might put together on a table top using some sticks and glue and pins and string
and maybe an egg and a couple of metal weights and a little race car that you stole from your brother. So there is
a vague idea of a *system* as some stuff brought together. And now to make it *dynamical* just means you set it 
up so that when you give it a push it does something interesting. It changes with time. 


Now that you know what a dynamical system is let's go back to chaos. A chaotic dynamical system is one that
is very very difficult to predict what it will do. In fact what it does depends on how you set it up at the 
start; but very microscopic changes in how you set it up can produce wildly different end results. 


Now what about fractals? Fractals are structures that are similar to themselves on different scales of size.
If you took a stamp of a foot outline and using a bunch of stamping actions drew a picture of a foot: That 
is getting into the idea of fractals. 


Now there is a strange thing about mathematics -- the study of patterns -- that chaos and fractals are connected
together. And this has everything to do with the deep mysteries of the universe that we don't have time to explain 
here. But I did want to tell you just these few terms { 'chaos', 'dynamical system', 'mathematics', 'fractal' }
so that you would have little buzzy wires with sparks coming out in your mind
as you work on this project. If the word 'philosophy' means 'understanding of the universe' then supposing things 
are complicated we can't learn everything at once. Hamlet says...


> There are more things in heaven and earth, Horatio, than are dreamt of in your philosophy. 


Again: If you would like to get started on the project ideas (there are three here) just skip down to where it 
says **Project 1** or **Project 2** or **Project 3**. Or just keep reading. Next it is pirates.


### Randomness and Probability


We begin with a story.


The town of Monte Carlo is located on the northwestern coast of 
the Mediterranean Sea. It is famous for its sunny weather, beautiful scenery and for 
gambling casinos where one can play games of chance like dice or roulette. Now as you know
rolling a dice is a probability experiment: You never know in advance what will come up.


One fine day a pirate named Sue who has been attending a party feels tired and returns to the harbor
to fall asleep in her hammock on board her boat. She arrives at the wharf where
her boat is secured. She sees it where she left it at the far end of the wharf. 
(A *wharf* goes out from shore and boats tie up to it.) This wharf is 21 steps wide and 
100 steps long; she she is 100 steps from her boat now. Unfortunately she banged her head on
an anchor a moment ago. The anchor was secured to another boat and she didn't see it in the dark harbor. 
She is now quite dizzy. 


Sue's boat is 100 steps away; so she begins walking.
The problem is that (being terribly dizzy) after every step forward towards her ship 
she stumbles sideways: Either to her left or to her right: One step sideways at random. 
She must make 100 forward steps to reach her boat. However if she takes
too many random steps to the left or to the right -- you see the problem -- she will tumble
off the side of the wharf into the cold water.
What is the probability she will make it safely to her ship at the far end of the 
wharf? Again: Sue starts at one end of the wharf centered left-right. She must go forward 
100 steps and if she ends up 11 steps to the right or left she falls off the edge
of the wharf into the water.


#### Project 1


The first project idea here is to solve this problem using a computer to simulate her 
walk down the wharf. If you do it once she might make it; or she might fall off the side.
This does not give you the answer 'what is the probability she makes it?' So think 
about this: What do you need to do in order to answer the probability question?



### Egon


Please meet Egon, one of my personal heroes. He appears different to everyone who meets him; and for me he is 
a slightly crazy artist (with a beard) who lives in Monte Carlo. This part of my Monte Carly story is
related to the previous one about the pirate except nobody is going to fall into 
the harbor. 


Egon is a painter and a poet. He lives in an apartment in Monte Carlo near the center
of town by the town square. This is a large flat plaza paved with bricks. Egon wishes to paint something 
on the bricks of the town square that somehow represents random chance so he ponders for some time. 
As he ponders Egon happens to notice there is a single dice in his beard. Egon rolls the dice; 
it comes up **4**. He keeps rolling; and of course each time he gets a number from one to six. 
Egon considers this and finally he hatches a plan. 


- Egon places three empty paint cans A, B and C in the town square to make a huge triangle
- He steps over to the side of the town square away from his three empty paint cans
- He rolls his dice: It is a **5**
  - On a **5** or a **6** his rule is: Walk half-way to can **C** and paint a dot
    - So Egon does just this. (He is carrying another can of paint and a brush.) 
- Egon has painted one dot so far...
- He rolls his dice again: It is a **1**
  - He walks half-way to paint can **A** and paints a dot
    - He has now painted two dots
 - He rolls his dice again: It is a **1**
   - He walks half-way *again* to can **A** and paints a dot


So you can see that Egon can amuse himself for many many hours, even days, rolling his dice, walking half-way to 
one of his three paint cans **A**, **B**, or **C** and painting a dot. 


The question for you is: What does the resulting painting look like? Feel free to think about this question for 
some time if you like. 


#### Project 2


Write a computer program to recreate Egon's painting. Since Egon uses a dice you may certainly use the Python random
number generator.


#### Project 3


Modify your program from Project 2, for example: 

- Egon may select any number of paint cans to place out in the town square
- Egon may choose a different "percent" of the distance to travel. Up above it was 50%, or half-way to the paint can. No reason this couldn't be 27% or 94% or even 212% or -71%
- The paint cans could be placed evenly like the vertices of a regular polygon... or they could be placed randomly


Hopefully by the time you have completed these three projects you have improved your Python skills. Did you 
learn anything interested that relates to the idea of fractals? 

