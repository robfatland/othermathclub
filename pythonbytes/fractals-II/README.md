# PythonBytes Project In-Depth


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/fractals-II#pythonbytes-project-in-depth)


### Overview


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/fractals-II/juliaset.png" alt="drawing" width="300"/>

Here is the 
[link to the simpler fractal project](https://github.com/robfatland/pythonbytes/tree/master/projects/fractals-I#pythonbytes-project-in-depth). 


This project begins with defining a new kind of number and some associated arithmetic rules. In particular we need both 
addition and multiplication. You are accustomed to real numbers like 4.3 and -19.83838383831111. So let's create a new
number that is simply two real numbers in a row like this: (4.3, -19.8383838383838381111). This -- you might say -- is not 
a number! It is two numbers in parentheses separated by a comma! This is true. But if we can come up with some good rules
for arithmetic then we can also say it is a new kind of number, a complicated number, even sometimes called a **complex** 
number. 

A complex number we write abstractly as **(a, b)**. Another one might be **(c, d)**. Let's define adding them in the 
most obvious possible way: 


(**a**, **b**) + (**c**, **d**) = (**a** + **c**, **b** + **d**)


Now we need a rule for multiplication. This will be a bit more *complex*:


(**a**, **b**) * (**c**, **d**) = (**a** * **c** - **b** * **d**, **a** * **d** + **b** * **c**)


With this we are ready to build some fractals... almost. We also need the idea of the absolute value of a complex
number. The absolute value of 7 is 7. The absolute value of -4  is 4. The absolute value of a complex number is the
length of the hypotenuse of a right triangle whose legs are **a** and **b**. Let's call that **S** for *Size*:


**S** = square root (**a** * **a** + **b** * **b**)


Now we have everything we need. Notice that a complex number (**a**, **b**) can be drawn on a graph using the x-axis for 
the first number **a** and the y-axis for **b**. Here is our plan: We will use two ```for-loops``` (nested) across x and y to
select one a whole lot of complex numbers one at a time. For each one we are going to draw a dot with some color. The color
of a dot will be red, orange, yellow, green, blue or black. We will decide which color using some calculations and a big ```if```
statement. 

The details are below. The main idea of this introduction is that you will be making a painting from colored dots that
chooses the colors using some arithmetic. 


### Details

First here is a description of what a Julia set program does; and we follow that with a recipe that you may consult.
You may also look at the program here called ```example.py``` if you would like some help.

#### Description

- Loop over coordinates: x should run -1.5 to 1.5, y should run -1.5 to 1.5. Go in small steps like 0.01
- Convert (x, y) coordinates to Turtle coordinates (i, j) which is on the turtle screen
  - The i coordinate will be -200 when x is -1.5; and it will be +200 when x is +1.5
  - The same rule applies to the j coordinate in relation to the y coordinate
- For each location z = (x, y) iterate the function z^2 + c some number of times (like 10) to arrive at a new number z'
  - c is some constant-valued number such as (0.3, -0.4). Notice c is a complex number.
- Calulate the ratio of the magnitude of z (mz) to the magnitude of z' (mz'): **r** = **mz** / **mz'**
  - If this ratio is less than 0.2 do nothing
  - If this ratio is greater than 2.0 make the pixel at (i, j) white
  - If this ratio is somewhere between 0.2 and 2.0 make the pixel some other color according to your preference
  
#### Recipe
  
Follow each step and test it to be sure it works. 
  
1. include the line ```from turtle import Turtle``` and declare a turtle ```t``` with speed 1000 and its pen ```up()```.
  
  
2. Include the line ```import math``` so that you can use the square root function
  
  
3. Define a tuple called ```c``` as the number ```(0.3, -0.4)```
  
  
4. Define a function that adds two complex numbers ```a``` and ```b``` according to the rule
  
```
result = (a[0] + b[0], a[1] + b[1])
```
  
Notice that ```a[0]``` is the first of the two real numbers in the complex number (tuple) ```a```. ```a[1]``` is the second.
  
  
5. Define a function that returns the square of a complex number z according to the rule

```
    return = (z[0]*z[0] - z[1]*z[1], 2.0*z[0]*z[1])
```

#### What next???


This is an advanced project. If you got this far on: Congratulations! You are truly an awesome and inspiring
Python programmer. To see the rest of the recipe please contact the Python Bytes club facilitators, particularly Rob.


