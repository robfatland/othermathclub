# The purpose of this program is to illustrate drawing from the matplotlib
#   perspective (not turtle). 

# AI in use: True
# trinket: OK | vscode: OK (renders live in a window via the TkAgg backend)
'''
Draw a stick figure person

Rendering note: this renders live in a matplotlib window using the TkAgg
backend. The default "agg" backend only writes to a file, so we select
TkAgg explicitly. This must happen BEFORE pyplot is imported, which is
why matplotlib.use("TkAgg") sits at the top of the module.
'''
import matplotlib
matplotlib.use("TkAgg")


def Person(x, y, h):
    from math import cos, sin, pi
    px, py = [x], [y]
    px.append(x+h/5);   py.append(y+4*h/9)
    px.append(x+2*h/5); py.append(y)
    px.append(x+h/5);   py.append(y+4*h/9)
    px.append(x+h/5);   py.append(y+(4/9 + 1/6)*h)
    px.append(x);       py.append(y+(4/9 + 1/6)*h)
    px.append(x+2*h/5); py.append(y+(4/9 + 1/6)*h)
    px.append(x+h/5);   py.append(y+(4/9 + 1/6)*h)
    px.append(x+h/5);   py.append(y+(4/9 + 1/3)*h)
    r = h/7
    cx = x + h/5
    cy = y+(4/9 + 1/3)*h + (1/7)*h
    for i in range(361): t = i * 2 * pi / 360; px.append(cx + r*sin(t)); py.append(cy - r*cos(t))
    return px, py


def DrawXY(x, y):
    from matplotlib import pyplot as plt
    ax = plt.subplot()
    ax.plot(x, y)
    plt.axis("equal")
    return ax


def DrawPerson(a, b, c):
    from matplotlib import pyplot as plt
    x, y = Person(a, b, c)
    ax = DrawXY(x, y)
    plt.show()   # live window via TkAgg
    return ax


if __name__ == "__main__":
    DrawPerson(0, 0, 9)


