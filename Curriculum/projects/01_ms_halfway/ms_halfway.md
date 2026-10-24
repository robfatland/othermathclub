# Ms Halfway


> For teachers: This can be done with or without Python; but it is a good intro
> to turning a process into code.


Laptops closed please.


Ms Halfway likes to take on tasks... but she invariably only completes half the
task at hand. If you ask her for a sandwich she will invariably give you half a
sandwich... so if you want an entire sandwich you had better ask for two!


Ms Halfway lives in a house at location 0.0. She wishes to mail a letter at the 
post office one kilometer away, at location 1.0. She decides to walk to the post
office... and so she starts out. But true to form she makes it halfway and decides
the post office is too far away after all... and so she stops. She thinks "Actually
I think I will just go home." So she starts off again... but when she reaches 
location 0.25 she stops. "No I think I'd rather be back at the halfway point
*where I just left from*", she thinks. And so she starts out again... but stops at
location 0.375 (which is 3/8).


Ms Halfway continues in this manner, always deciding to go back to where she 
just was. Each leg of her journey is half as long as the previous leg. And
you can imagine that eventually her journeys become so tiny they amount to 
a fraction of a step. Eventually no actual motion all! The question is -- and
this is very important -- when Ms. Halfway eventually comes to a halt: Where
is she, location-wise? She must be at a location greater than 0 but less than 
0.5. 


> For teachers: The above is fun to enact, and even re-enact with multiple 
students. We use orange athletic field cones to mark off progress when we can.
So its not a super involved kinesthetic; but it does help.


In 2026 I shifted the teaching to begin with a function. Why not? Let's make
functions part of the vocabulary from day 1. The really mind-bending aspect is
that this first function expects variables `a` and `b` but we are sending it
values `h` and `d`. This makes functions harder to comprehend because the 
function gets to use its own naming (namespace is the eventual term) and this
matches up to the eventual function *call* by slots. But not by names. 


Here is the top of the program:


```
def average(a, b):
    return (a + b)/2
```

Now we spend 10 minutes talking about averages: How they are calculated; and
we draw a table.


| h | d | average | x |
| --- | --- | --- | --- |
| 0 | 2 | 1 | 1 |
| 6 | 10 | 8 | 8 |
| 13 | 15 | 14 | 14 |
| 9 | 5 | 7 | 7 |
| 4 | -4 | 0 | 0 |


Each line is "Ms Halfway is at 0, her destination is 2. What is the average? (1) Where does she end up? (1).
After doing a bunch of these we can make the point that Ms Halfway will end up at the *average* of her
location and her desired destination. This is why we created the `average()` function. 


> Teaching note: Without the average function the code for calculating where Ms Halfway winds up gets
tortured and difficult to follow: Because of the changing sign of her direction. So we circumvent 
that complexity without letting on to the students. This does make the progress from story to code 
a bit longer so be prepared for a journey. 


In terms of project arc (to interrupt the narrative for a moment):


- Ms Halfway: Gets us functions, variables, `print()`; and the idea of copy-paste code to repeat an action
- Fibonacci: Very similar to Ms Halfway, acts as a "apply what you learned"... and only now do we introduce loops
- Turtle: This seems harmless, a way to draw on the screen
- Probability: Random number generator, random walk scribbles
- Monty Hall: Putting RNG to work, counterintuitive logic, validation by code
- Chaos: A random process leading to a very orderly structure (Serpinsky gasket: version 1)



## Variables

- `h` — where she is
- `d` — where she wants to go
- `x` — the unknown: where she ends up (the halfway point between `h` and `d`)



## First program


Create and run this program... make sure that it prints `0.5`.


```
def average(a, b):
    return (a + b)/2

h = 0
d = 1
x = average(h, d)
print(x)
```


After computing and printing `x`: Ask the student to calculate where she ends up after her second 
journey. Students will tend to go for the right answer because they are new to the idea of *method*.
For example they might add:


```
y = average(x, d)
print(y)
```


If they keep on this way eventually they will see "there has to be a better way". This is the 
point where we can introduce updating the variables after `x = average(h, d)`. 


We can say "Ms Halfway's location has changed: She is now at `x` so we say `h = x`. 
In like fashion we can update `d` to be where she just was: `d = h`. 


But there is a problem: In this order `h` has been overwritten so `d = x`. We have to
go in the opposite order: 


```
d = h
h = x
x = average(h, d)
print(x)
```


Now these four lines of code follow the first print statement and we see `0.25`. 


Now we say "Let's keep going by copy-pasting those four lines of code." Students can
verify for however many pastes they do that the location `x` is sensible. And 
eventually they will figure out where it is Ms Halfway winds up. 


Emphasis: I do not introduce loops here because we already have a *lot* of moving
parts. Instead by not mentioning loops we hopefully generate a sense of how 
*inconvenient* it is to make code repeat by cut-and-paste.


Once we have Ms Halfway sorted out: Write Fibonacci.py and be sure to revisit
the importance of the **function** (this time call it `addemeup(a, b)` because
`sum` is already a keyword in Python and we do not want to clobber it.) Also 
in Fibonacci three variables will suffice and the order of update is important. 
So Fibonacci is a slightly simpler version of Ms Halfway that the student who
is catching on should be able to pretty much on their own.


End note 1: The mathematical solution to Ms Halfway:



$x = 1/2 - 1/4 + 1/8 - 1/16 + 1/32 - \dots$


$\frac{1}{2}x = \;\;\;\;\;\;1/4 - 1/8 + 1/16 - 1/32 + \dots$


Write these one above the other and draw a line under them. Write a big plus sign at the left. Add them up: The left side and the right side.


$\frac{3}{2}x = \frac{1}{2}$


$3x = 1$


Hopefully this leads to $x = 1/3$.



End note 2: Ms Halfway had an asymptote at 1/3. Fibonacci keeps getting bigger
but it does have an asymptote in the ratio of successive terms. This makes a
nice bonus project for students who are up for more challenges.