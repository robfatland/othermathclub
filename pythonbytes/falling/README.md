# Falling From The Sky For Beginners


Some people think that falling out of the sky is easy. Not so! How do you get to the top of the sky in the first place? 
Once you are falling: What will you remember that you wish you had brought with you???


This is a Curriculum lesson (not Project work). We will do a code-along Zoom call to create graphics of things falling.


The following week we will do **Rule 18**. What is Rule 18? I can't tell you here. 
[The Rule 18 homework assignment is at this link.](https://github.com/robfatland/pythonbytes/blob/master/homework/README.md)




## Various fallings


* Fall straight down to the ground and land with ***WHAM!!***


* Fall more slowly on a parachute and land in the ocean. 
    * Use random numbers to drift back and forth
    * Use a list to create a thoughtful message as you drift down


* Single Meteor fall
    * Very fast! Streak down from the sky!
    * Little bit of sideways motion but very little compared to the parachute above


* Bolide Meteor fall
    * Same idea as meteors: Fast, just a little random side to side
    * However: Bolides break apart into pieces


## Additional ideas


Talk on slack to learn more!


* Draw Nereocystis
    * At the top it is large flat ribbons
    * Then there is a bulb
    * Then a stalk that tapers on the way down
    * Then a dense root structure called a holdfast
   
   
* Space Invaders (not the arcade game)
    * Like bolides but with a data structure
    * Starts out with one space invader
    * A space invader has a certain probability to split in two as it falls 

* Rule 18
    * This is a more careful version of Space Invaders that uses cells

* One Dimensional Cellular Automata
    * Extends Rule 18


## Fall Straight Down

* Write a program that writes the word "me" in the middle of the screen 30 times in a row. 
    * This is supposed to look like "me" is falling
    * At the end print `WHAM!!` underneath the last `me`, and then use `-----------------` to represent the ground

Congratulations! Now let's make it more realistic.

* Import sleep by putting at the top of the program the line `from time import sleep`
* After each print statement add the line `sleep(0.3)` so that the fall is a little bit slower

Now it looks more like `me` is falling

* Use a loop to print **me** falling, like this:

```
for i in range(30):
    print("   me")
    sleep(0.3)
```

Now let's use parameters. Notice there is the number 30 and the number
0.3. It is more flexible to use parameters.

```
number_of_me_prints = 30
pause_time = 0.3
```

Now you can write the `for-loop` as `for i in range(number_of_me_prints)`. Can you figure out how to modify
the `sleep(0.3)` to make use of the `pause_time` parameter? 

Ok two more things we need to do. First: Let's put everything inside a function called `FallFromTheSky()` like this:

```
def FallFromTheSky():
    all
    of
    the
    code
    you
    wrote
    above 
    goes here

FallFromTheSky()
```

Now why does this work? Because the last line calls back to the first line and tells it to do what it knows how to do. 

Last item: Let's make our `print()` print a string called `message` and we will be tricky about how we create `message`.

```
    message = ' '*20 + 'me'
    print(message)
```

Notice that we multiplied a space `' '` by 20 which turned it into 20 spaces in a row. Hah! That's ridiculous. But it seems to work.


## Second version: Use a parachute


At the top of our program let us now import a random integer generator called `randint` like so: 

```
from random import randint
```

We will get to its use later on. 


Print `me` all the time is getting dull. 
Let's now create a list of strings that represent us thinking but not saying anything. 


```
thinking_list = ['...', '...', '...', '...', '...']
```

Now let's create a list of what we say out loud when we begin falling...

```
what_i_say_list = ['oh', 'dear', 'it', 'seems', 'I', 'am', 'falling', 'from', 'the', 'sky', 'again']
```

And now we shall begin falling. The number of falling steps above was 30. This time we are going 
to make the number of falling steps be just long enough to print the `what_i_say_list`. To do this
we need to know the length of this list (which as you can see is 11). For this we use the 
keyword `len` which is short for **length**. 


```
number_of_prints = len(what_i_say_list)
print("I have", number_of_prints, "words to say as I fall")
number_of_spaces = 40
pause_time = 0.4

for i in range(number_of_prints):
    message = ' '*number_of_spaces + what_i_say_list[i]
    print(message)
    sleep(pause_time)
```

Now when we run this program we gently fall to earth saying what we think. 

Up above we created a *thinking* list also; but we did not use it yet. So now 
let's **extend** the `what_i_say_list` to include a period of thinking after the speaking.
Where should we insert this line of code in the program? 

```
what_i_say_list.extend(thinking_list)
```

Notice that the list has a built in function (or *method*) called `.extend()` that makes the list longer.
It glues the elements of the `thinking_list` on to the end of the `what_i_say_list`. What is cool is that
this should also run properly; so go ahead and run it to test. 

Next let's add two more spoken messages and one more thinking message like this.

```
second_spoken_message = ["oh", "but", "this", "time", "I", "cleverly", "brought", "along", "my", "parachute"]
third_spoken_message = ["that", "looks", "like", "the", "ocean", "down", "there", "oh", "my"]
```

Now extend the `what_i_say_list` to include `second_spoken_message`, another copy of `thinking_list`, 
and `third_spoken_message`. Make sure that works properly whene you run it. 


Finally we do not yet drift back and forth as we would if we were really wearing a parachute. For this
let us use the `randint(-2, 2)` function. This will give us a random number from `-2` to `+2`. Here 
is one way to code this: 

```
number_of_spaces = 30
```

just as above. However now inside the loop we change number_of_spaces by a random amount. 
We add one more line of code after the `sleep()` line: 

```
    number_of_spaces = number_of_spaces + randint(-2, 2)
```

My final program looked like this. Notice I put in a splash at the end.

```
from time import sleep
from random import randint

what_i_say_list = ['oh', 'dear', 'it', 'seems', 'I', 'am', 'falling', 'from', 'the', 'sky', 'again']
second_spoken_message = ["oh", "but", "this", "time", "I", "cleverly", "brought", "along", "my", "parachute"]
third_spoken_message = ["that", "looks", "like", "the", "ocean", "down", "there", "oh", "my"]
thinking_list = ['...', '...', '...', '...', '...']

what_i_say_list.extend(thinking_list)
what_i_say_list.extend(second_spoken_message)
what_i_say_list.extend(thinking_list)
what_i_say_list.extend(third_spoken_message)

number_of_prints = len(what_i_say_list)

print("I have " + str(number_of_prints) + " things to say as I fall\n\n")

number_of_spaces = 40
pause_time = 0.4

for i in range(number_of_prints):
    message = ' '*number_of_spaces + what_i_say_list[i]
    print(message)
    sleep(pause_time)
    number_of_spaces = number_of_spaces + randint(-2, 2)

print(' '*(number_of_spaces  - 2) + 'SPLASH!!!!!!')
print('~'*90)
```





## Third version: Single Meteor Fall


The meteor mostly falls vertically but goes very fast, and every so often moves a bit to the left or right.
The challenge here is to make use of `randint()` in a controlled way so there is just a little bit of sideways motion.


## Fourth version: Bolide Meteor Fall


A bolide is a bright meteor that sometimes fragments into pieces. So just as above with the meteor but has a 
chance of splitting in two. Then there are two fragments to track. And they may split also... and so on. 

One way to do this is to decide in advance how and when each piece splits in two. For example you might
decide that the original meteor falls for 30 lines of text, then splits; and these two fragments fall for
27 more lines, and one of them splits so you have 3 fragments that fall for another 42 lines. 


## Fifth version: Nereocystis


This is drawn on just one screen; there is no falling. Research the word *nereocystis* to learn more!


## Sixth version: Space Invaders


## Seventh version: Rule 18

18 in powers of 2 is 16 + 2. That is, 2 raised to the 1 power plus 2 raised to the 4 power. As an 8-digit binary number 
it is 0 0 0 1 0 0 1 0. 

Suppose we have a list of cells. Each cell contains a 1 or a 0. We can print this out on the screen if we so desire. 

Now we introduce a clock that is going to tick forwards in time.  Each tick of the clock changes the list of 0s and 1s. 


## One Dimensional Cellular Automata


This builds on Rule 18 above.

