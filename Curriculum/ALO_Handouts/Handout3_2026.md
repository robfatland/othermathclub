# Loops: Better than copy-paste


To solve Ms Halfway we copy-pasted a 4-line code block over and over. You may think we should just tell Python to repeat just one code block a bunch of times. And you would be absolutely right. Code that loops is called a *loop*. Remember Handout 2?  We did some turtle drawings? At the very end of the program we used a loop to draw a spiral. Here are more loops to get you used to them. 


Predict what gets printed first for each for loop. Then run it to see. (DO THESE ONE AT A TIME!!)


```
for i in range(4):
    print('jello weird')

for i in range(11):
    print(i)

for i in range(9):
    print('jello weird', i)

many = 6
for i in range(many):
    print('jello weird', i, many)

for i in range(3):
    print(i * 2)

for i in range(7):
    print(i + 3)

for i in range(6, 12, 2):
    print(i)

for i in range(1000, 990, -2):
    print(i)

for j in range(6):
    print(i)

for j in range(6):
    i = j + 3
    print(i)

h = 0.
d = 1.
for i in range(10):
    x = (h + d)/2
    print(x)
    d = h
    h = x

total = 0
for i in range(1, 7):
    print(i)
    total = total + i
print(total)

# a loop inside a string
for i in range(1, 6):
    print('star ' * i)

# notice the pattern from handout 1 again
for i in range(20, 31):
    print(i % 3)

# a loop that waits for you
for i in range(3):
    print(i)
    s = input("tap enter")
```


Your turn: Write a loop that counts down from 10 to 1 and then prints `blast off`. Extra challenge: use a loop to print a triangle of stars that grows one row taller each line.
