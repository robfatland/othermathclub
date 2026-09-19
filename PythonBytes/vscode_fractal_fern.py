from turtle import Turtle, tracer, update

t = Turtle()

tracer(0, 0)

t.hideturtle()
t.pencolor("#ff0000")
t.penup()

x0 = 200
y0 = -100
heading0 = 90
level0 = 0

width0 = 25
nSegments = 20
forward0 = 80
segmentTurn = 24
reductionRate = 0.83

mywork = [(x0, y0, heading0, level0, width0, forward0)]

level = level0
maxlevel = 3
branchscale = 0.3
forwardscale = 0.6

while level < 3:
    if len(mywork):
        x, y, heading, level, width, forward = mywork.pop(0)
        t.penup()
        t.setpos(x, y)
        t.pendown()
        t.setheading(heading)
        t.width(width)
        for i in range(nSegments):
            t.forward(forward)
            t.left(segmentTurn)
            
            newlevel = level + 1
            if newlevel < maxlevel:
                newx, newy = t.pos()
                newheading = t.heading() - 90.
                newwidth = width * branchscale
                newforward = forward * forwardscale
                mywork.append((newx, newy, newheading, newlevel,
                               newwidth, newforward))
            

            width = width * reductionRate
            t.width(width)
            forward = forward * reductionRate
    else: break
    
update()
input('hit enter   ')
