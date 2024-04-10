# PythonBytes Project In-Depth


## Maze


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/maze#pythonbytes-project-in-depth)


### Overview


Let us define a maze. It will consist of one entrance and one exit. Once you enter you follow a hallway to a room with one
or more hallways leaving from it. From each room there will be a maximum of six hallways (including the one you 
just came in on). From one of the rooms -- you do not know which one -- there is a hallway leading to the exit. Once 
you go down that hallway you leave the maze and win the game. 


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/maze/maze.png" alt="drawing" width="350"/>


Here is a pretty easy maze. If instead of 10 rooms if it had 1000 rooms it might be harder to solve. Notice it includes a loop
so if your algorithm was simply 'take the first hallway to the left' you would never escape.


This is a fun programming challenge because it has three parts to solve? First how do we define the problem in terms of 
programming, in terms of Python code? Second how do we watch it play out on the screen? Third how do we debug or improve 
the escape algorithm?


As to the first part: We will begin by providing you with four test mazes. They
get progressively more difficult. The code you write to navigate them we will call the **Solver**.


As to the second part: We will describe a simple turtle graphics method for tracking your progress. 


As to the third part: Let's see how the first two parts go first!


### Details


We will save complicated mazes for later. For right now we will say that the maze consists of 25 rooms layed out in a 
5 x 5 grid. Some rooms may be connected, others might not be (so they are not part of the maze). Let's number the 
rooms 1 through 25.

```
0 --  1     2     3     4     5 
      |
      6 --  7     8     9    10 
            |                          A very simple maze... as an initial test of a solver
     11    12    13    14    15 
            |
     16    17    18    19    20 
            |
     21    22 -- 23 -- 24 -- 25 -- 26 
```

The starting location will be room 0 which has one hallway leading to room 1 on the corner of the maze.
Room 25 on the opposite corner will feature a hallway that goes to room 26, the exit. 


So you start out in room 0. How do you go to another room of the maze? You call a Python function called ```mazemove(r, x)```. 
Notice you are passing two arguments to the function mazemove(): ```r``` and ```x```. This function will return a result which
will be the results of your move. 



Here is the second test maze which makes sure your solver can go in all possible directions (still very easy).


```
0 --  1     2 --  3 --  4 --  5 
      |     |              /
      6 --  7     8     9    10 
               /     \     \           A slightly more complicated simple test. Room sequence
     11 -- 12    13    14 -- 15        is 0 1 6 7 2 3 4 5 9 15 14 8 12 11 16 21 17 18 19 25 26
      |                                Notice there are no branching choices. 
     16    17 -- 18 -- 19    20 
      |  /                 \
     21    22    23    24    25 -- 26 
```


The third test maze features some branching, a loop, and some dead ends.


```
0 --  1 --  2 --  3 --  4 --  5 
                           /  |
      6 --  7 --  8 --  9    10 
            |           |     |        A more difficult test. Room 5 features the option to go to room 9...
     11 -- 12    13    14    15        Solution is 0 1 2 3 4 5 10 15 20 25 26. If you go to room 9 you have
      |     |           |     |          a loop and some dead ends to escape from... you need to get back to
     16    17 -- 18 -- 19    20          room 5 to make further progress.
      |     |                 |
     21    22 -- 23 -- 24    25 -- 26 
```


