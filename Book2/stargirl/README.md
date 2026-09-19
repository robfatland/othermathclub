# PythonBytes Project In-Depth


[Link to here](https://github.com/robfatland/pythonbytes/tree/master/projects/stargirl#pythonbytes-project-in-depth)


### Overview


A certain billionaire has trapped you, Stargirl, on a Tesla Roadster headed towards Jupiter. If you are very careful
you can use your last few ounces of rocket fuel to fine-tune your arrival. Use your computer (and some Python) to
predict the proper entry path that will put you on a gravity-assist slingshot escape trajectory back towards the 
earth. 

![stargirl](https://github.com/robfatland/pythonbytes/blob/master/projects/stargirl/stargirl.png "Stargirl far above the moon")


This project is not for the faint of heart; I would say it is advanced. One way to approach the programming
challenge is outlined below. As always it may help to consult with us, your Python Bytes coaches and teachers.
Our first suggestion: Do the project on **Bugs** first. This project is an extension of that one.


### Details


The sketch of ideas goes like this...

- Work in only two dimensions: A flat piece of paper (or in geometry: a plane)
- Establish the location, mass and radius of Jupiter (easiest to put Jupiter at (0, 0))
- Establish the locations, masses and radii of Io, Europa, Callisto and Ganymede
- Establish a series of starting locations with velocities (possible entry points of your spaceship)
- Use simple physics of gravity to travel forward in time


![trajectories](https://github.com/robfatland/pythonbytes/blob/master/projects/stargirl/trajectories.png "Stargirl trajectories")


### Time

If you think about it you might decide that the reason we have *time* is so that everything doesn't happen at once.
In the case of a space ship: It might start out at some location (like a turtle in turtle graphics) with some
direction of motion. Perhaps a second ticks by on the clock and the space ship moves in that direction a certain
distance: Based on how fast it is moving. 


Now suppose you are moving through space in this way, far from any objects like planets. There is nothing
pulling on you and so you continue in a straight line. Unless you turn on your rocket motor you will neither
speed up nor slow down nor veer off in some new direction. 


But wait! Up ahead and off to the side a bit there is a planet. It exerts a gravitational pull on you that
causes your space ship path to bend or curve. This gravitational pull becomes stronger the closer you get
to the planet; but it does not automatically mean you will crash into the planet. Your path curves but perhaps
you still miss the planet. 


Now what if there are two planets up ahead? Of course they *both* exert a gravitational influence upon you...
so to calculate how your course changes you must add together the influence of planet 1 to the influence of 
planet 2. 


In order to turn these ideas into code we have (or actually *will*) create a notebook here for you to look at. 


As with 
