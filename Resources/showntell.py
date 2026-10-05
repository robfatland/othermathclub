'''
Draw a stick figure person
'''
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
    x, y = Person(a, b, c)
    return DrawXY(x, y)
