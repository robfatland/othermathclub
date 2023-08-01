# PythonBytes Project In-Depth


## Knight's Tour


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/knight#pythonbytes-project-in-depth)


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/knight/knight.png" alt="drawing" width="350"/>


### Overview

A chess knight hops two squares across plus one square over. A famous question is whether the knight can hop to each 
square of the 8 x 8 chessboard once in 63 moves; and the answer is 'Yes!'... but how? 


This project is an opportunity to explore recursive functions; which are functions that call themselves. 


Here are the first ten squares of a knight tour across an 8 by 8 chessboard.


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/knight/tour10.png" alt="drawing" width="400"/>


That is: The knight has started at the upper left square and made nine hops so far. 


### Recursion


Both this project -- the knight's tour -- and the Sudoku project can make excellent use of the principle of *recursion*.


To illustrate how recursion works let's think about a simple program. Read the code and try to decide in your mind what it does...


```
# What will this program print out? 
def recursion(a): 
    if a == 0: return a
    return a + recursion(a-1)
    
answer = recursion(7)
print(answer)
```

This program will print out **28** and the logic of how it runs is instructive. 

* ```def recursion(a):``` defines a function (but does not run it yet)
* ```answer = recursion(7)``` will run the recursion() function and the next line prints out that answer
* Let's track what happens when ```recursion(7)``` runs...
  * ```recursion(7)``` evaluates **a** is not zero so it returns (instead) the value **7 + recursion(6)**
    * Before this value can be returned: recursion(6) must execute...
    * ```recursion(6)``` evaluates **a** (now 6) is not zero and so it returns **6 + recursion(5)**
    * As before ```recursion(5)``` must run before ```recursion(6)``` can return
      * recursion(5) returns ```5 + recursion(4)```
        * recursion(4) returns ```4 + recursion(3)```
          * recursion(3) returns ```3 + recursion(2)```
            * recursion(2) returns ```2 + recursion(1)```
              * recursion(1) returns ```1 + recursion(0)```
                * Since **a** equals 0 at long last recursion(0) returns 0 without calling recursion()
                  * ...so all the earlier versions of recursion() will start getting answers back...
                  * ...so that they too may return
              * So now the zero is returned to recursion(1)...
                * and recursion(1) returns 1 + 0, in other words it returns 1
            * So recursion(2) returns 2 + 1 or 3
          * So recursion(3) returns 3 + 3 or 6
        * So recursion(4) returns 4 + 6 or 10
      * So recursion(5) returns 5 + 10 or 15
    * So recursion(6) returns 6 + 15 or 21
  * So recursion(7) returns 7 + 21 or 28
  * And at last this value of 28 is assigned to **answer** and we are done
  
Notice that at its peak we had 8 different version of the ```recursion()``` function running. Each one was 
separate from the others. When ```recursion(7)``` called ```recursion(6)``` it created a totally new version
of the function in addition to itself. 


* To get some practice with recursion try writing a factorial program that multiplies numbers together. 
```1 x 2 x 3 x 4 x 5``` is 5-factorial, also written **5!**.
* Write another recursion program that tells you what the 10th prime number is. 


### Recursion in the knight's tour problem


The knight's tour problem is really a fairly difficult challenge. The reason is that it is easy to get stuck.
The knight can at first hop to just about any square because the board is empty. However as the squares are 
visited they become no longer available; and the knight has fewer and fewer options. 


You can imagine using a recursive function that calls itself to try and make the next hop in the sequence.
The difficulty comes when the knight lands on a square with no moves available. The knight must back up
to an earlier point in the tour and take a different path. It is rather like running a maze where you are
putting up the obstacles of the maze as you go... and sometimes in running a maze it is necessary to backtrack. 


In the Sudoku project the challenge is similar: You can proceed to guess values for the Sudoku cells until
you either come to the end of the puzzle (yay you solved it!) or until there are no available options for
a cell that is still empty. The rules forbid all nine choices; and so as with the knights you must back up
and try another option. 


Because these projects are quite challenging we encourage you to discuss them with the coaches; and to try out
simpler problems first. Below is a list of recursion problems.

* Adding up integers
* Multiplying integers (factorial)
* Adding up prime numbers below 1000
* Solving a gallon puzzle (see the coaches for how this works)


