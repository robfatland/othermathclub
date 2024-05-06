# Sudoku


This page describes a Sudoku solving computer program.


First we need a nice way of writing a Sudoku puzzle. This will be 81 characters where blank cells are '0'. 
We do this like a book reading left to right, top to bottom. So here is an example Sudoku puzzle translated
into a string:


```060000008201800500905002000000704602300090005504608000000900301007005906100000050```


Here is how Sudoku looks usually of course: 


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/sudoku/sudoku2.png" alt="drawing" width="300"/>


Now the idea is for a Python program to read in the string version, crunch away on it, and print out the Sudoku solution. 


## Recursion


Go to [this link](https://github.com/robfatland/pythonbytes/tree/master/projects/knight#recursion)
and learn about recursion. Don't forget to do the exercises!



Let's not use a *string* type for the puzzle in our Python program. Strings are difficult
to modify; so we will use something more flexible.


The nice thing about using Python is that the program keeps track of everything.
Therefore for a celebratory moment: Not only are we capable of imagining 
such a difficult puzzle to solve; we can also come up with an efficient way 
to solve it and use the structure of the computer to do the tedious work...
very quickly.


A Sudoku puzzle is 9 x 9 cells or 81 cells. Therefore we could represent a puzzle using
a string of 81 characters. In Python strings are a **type** of variable; but they are difficult 
to change... 
We can only change strings by building new strings from them which is slow and klunky. 
The thing in Python that is easy to change is called a **list**.  Therefore let's 
use a string to describe the Sudoku puzzle at the start; and then let's convert this string into lists that we 
can work with. 

Our first puzzle we have as a string already:


```
p1 = '060000008201800500905002000000704602300090005504608000000900301007005906100000050'
```


Here just to check our skill a little further is another puzzle.


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/sudoku/sudoku.png" alt="drawing" width="300"/>



Here is another puzzle:


```
..86324..                                       008632400
.4.....1.                                       040000010
5..9.4..6   --------------------------------->  500904006
8.......5                                       800000005
6.......4            zeros for blanks           600000004
1.7...9.2                                       107000902
4..751..3   --------------------------------->  400751003
.6.....2.                                       060000020
..58267..                                       005826700
```


And we connect them all together in a single string to represent the Sudoku puzzle:

```
p2 = '008632400040000010500904006800000005600000004107000902400751003060000020005826700'
```


### Solver ideas


The cells can be numbered in Python fashion from 0 to 80 (as there are 81 of them). 
However each cell has a unique (row, column) address. 
The upper left cell is (0, 0) and has index 0.
The lower right cell is (8, 8) and has index 80. 
The center cell is (4, 4) and has index 40.
The lower left cell is (0, 8) and has index 72.





An empty cell in the puzzle string is a '0' zero character. This is fine but
it does not give us information about what *could* be written in that cell. 
So when we get to the business of solving the puzzle let us instead represent an empty 
cell of the puzzle as a **list** of possible numbers that could
be written in that cell according to the three Sudoku rules. 


For example cell (0, 0) of the first puzzle **p1** could have any of the nine digits so we make this list:


```['1', '2', '3', '4', '5', '6', '7', '8', '9']```


However the rules of Sudoku tell us some of these are forbidden: 
* 1, 2, 5, 6, 9 from the cell block numbers in the puzzle
* 1, 2, 3, 5, 9 from the column
* 6, 8 from the row


The correct list of possible values is therefore: 


```['4', '7', '8']```



This is the last bit of bookkeeping: Every cell has its own set of *related* cells per
the rules. These are the cells in the same *row* as that cell, in the same *column* as 
that cell, and in the same *block* as that cell. 










