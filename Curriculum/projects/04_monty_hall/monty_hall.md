# Monty Hall


To write this code we want to learn and understand `random.randint(a, b)` and we need an 
introduction to `if` logic. 


Mystery question: What is this code equivalent to? `print(randint(1, 6))`


`if` logic is a matter of working a lot of simple examples until it becomes
second nature; here is a template: 


```
if not 3 < 2: print("lurg")
else:         print("durg")
```


We are a contestant on a game show. There are three doors and a game show host named Monty Hall.
Behind one door, selected at random, is a million dollars. Behind each of the two remaining doors
is a goat. Monty knows... but we do not.


Monty asks us to pick a door... so we say "door 2". 


Monty shows us what is behind a different door, door 3: It is a goat. 


Monty says "Would you like to switch your choice to the other door?"


What should we do? 


The game *always* works like this: Monty will only ever reveal a goat behind a door we did not pick.


Let's call the two strategies "switch" and "stay". We can create a simulation of the game
and play it many times with each strategy to find out which one works better... or maybe 
it makes no difference. 


> Coach note: It is tempting to try and write code that enumerates cases. This is an 
opportunity to think on paper first rather than rushing to write out a bunch of if 
statements. To my surprise: Both strategies can be placed inside a for-loop in just four lines of code.