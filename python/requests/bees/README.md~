# PythonBytes Project In-Depth


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/bees#pythonbytes-project-in-depth)


### Overview

Farmers like to see bees (particularly honey bees) in their fields and orchards because the bees help pollinate the plants. 
In this project we imagine that you are such a farmer and you happen to own ten drones that you can send to locations in 
your orchard. By measuring the local buzzing your drones are able to tell you how many bees there are at that location. 
You goal is to determine places where the bees are clustering (these are called hives) so that you can visit those locations
in early summer and hopefully capture a swarm. 


Now what is a swarm? And why do bees do this behavior? And why would a farmer wish to *capture* it? (It sounds rather
dangerous!) And once they do is that good or bad for the bees? So who wins and who loses in this situation. We leave it
to you to do the research. For now we will concentrate on the programming challenge: Use Python to send your drones out 
into your orchard to observe the bee density. Use your intelligence to program a search pattern... but be warned: 
The further out you send your drones the more likely it is that they will become entangled in the branches of your
orchard trees and lost. 



### Details


Somewhere on the internet is a service that listens for requests ('How many bees are at (x, y, z) coordinates?') When it
gets such a request it returns the number of bees; but of course the answer will be somewhat at random, bees being what
they are. This is how we are simulating your drone observing the bees. However if your drone gets tangled in the orchard
branches the service will return the string 'drone lost'. 


You want to locate the bee hives so that you can transfer the summer swarms to Dadant hives. 
The project is to write a program that intelligently locates the hives before you run out of drones.  


What is a 'service'? First let's come up with a name for 'what you type in your browser window'. For example if you
type in 'google.com' your browser gives you a search window from Google. So let's call that thing you type in a URL.
You can read about what URL stands for on Wikipedia if you like. Suppose you want to go to Google to look up what
Dadant hives are. You can type in the URL http://google.com and then type in 'Dadant' in the search box. OR you can
use a different URL that does the search immediately. Try typing this into your browser: 


```
http://google.com/search?query=Dadant
```

What you did was tell Google some additional things by making the URL longer. Google interpreted what you put in
to mean 'Dear Google: Please do a search for me using the word *Dadant*'. And that is what Google did for you; and
that is what we mean by a *service*. 


Now here is a way of trying out the service that tells you how many bees are at ```(x, y, z)```. Try copying 
and pasting this: 


```
https://52t7suregg.execute-api.us-east-1.amazonaws.com/default/dronebees?x=12&y=16&z=4
```

I just did this and what I got back looked like a blank web page... until I noticed the number **8** in the upper left corner. 
So apparently there are 8 bees at the coordinates ```(x, y, z) = (12, 16, 4)```. So that's cool. What happens if I hit refresh?
The answer is that this time I got 5 bees. So it changes. As long as my searches are really close to the corner ```(0, 0, 0)```
like this it is unlikely I will lose my drone. So you can practice a bit, safely. 


Now what happens when I send the drone out into the orchard? Let's make a URL that sends a drone to location ```(1000, 1000, 30)```
which is just about the center of the orchard? Here is the URL to use for this: 


```
https://52t7suregg.execute-api.us-east-1.amazonaws.com/default/dronebees?x=1000&y=1000&z=30
```

What I got back after a few refreshes was **6**, **4**, **5**, and **drone lost**. So my drone got stuck in a tree. 
That's ok; I have 9 left. 


Now this is going to be very tedious; but tedious tasks are what computers are good at. So your job is to build 
a Python program that talks to the internet; in fact that talks to this service.  Here is what the code looks like.
(This will not work at cswonders.com in code pad by the way; you will need a different Python environment.)


```
import requests
def bees(x, y, z): return requests.get('https://52t7suregg.execute-api.us-east-1.amazonaws.com/default/dronebees?' + \
        'x=' + str(x) + '&y=' + str(y) + '&z=' + str(z)).text
    
print(bees(10, 17, 4))
```


When this runs properly it will either return a number of bees or it will return 'drone lost'. 


The challenge of this project is to think about the logic for locating the bee hives. If there was no danger of
losing drones you could just send the drone out four million times to every possible location in the orchard. 
However since the drones will eventually all wind up stuck in the baobab trees it behooves you to come up with 
a more efficient strategy.


Notice that you can augment your Python program with an incredibly powerful computer: You can use your own brain
to make suggestions by means of an input statement. 


