# AI in use: True  (extracted + header added during consolidation; logic by Rob)
# trinket: not tested | vscode: not tested
#
# Pursuit family — Wolf and Duck
# Extracted from a markdown cell in Resources/Coding2.ipynb ("gradient descent").
#
# A duck swims in a round pond of radius R at speed vd. A wolf runs around the
# shore at speed vw (faster) toward the duck's "shadow" (the shore point at the
# duck's current angle). The duck escapes by first spiraling out to ~R/4, where
# it can beat the wolf's angular speed, then breaking for shore.
#
# This version finds the escape path by GRADIENT ASCENT on a reward function with
# a plateau between an inner radius (~0.22 R) and the outer R/4 ring -- connecting
# pursuit to optimization. Uses turtle graphics, so it will not run under Jupyter.

from turtle import Turtle, tracer, update, Screen
from random import random
from math import sin, cos, pi, atan2, sqrt

R         = 250.                # pond radius
vd        = 1.                  # duck meters per second
vw        = 4.                  # wolf speed meters per second
dt        = 3                   # time step seconds
d_step    = vd * dt             # duck move distance in dt
w_step    = vw * dt             # wolf move distance in dt

# construct a reward function with a radial plateau
r_plateau = 100.                # this is the high reward "on the plateau"
r_bump    = 2.                  # margin of error
r_inner   = R*(1-vd*pi/vw)      # plateau inner radius: about .22 R
r_outer   = R*vd/vw             # plateau outer radius: precisely .25 R
r1 = r_inner + r_bump           # plateau defining radii with margin included
r2 = r_outer - r_bump
slope_inner = r_plateau / r1    # reward function slope inside the plateau
slope_outer = -r_plateau / (R - r2)                   # outside the plateau
intercept_outer = -R * slope_outer

angle_scale = 1         # relative scale of the angular reward function

omega       = 3*pi/2    # wolf starting location
wr          = R
wx, wy      = R * cos(omega), R * sin(omega)


dr = 0
theta = pi/2 - .01
dx, dy = dr * cos(theta), dr * sin(theta)

# Here we set up the graphical representation of the problem
#   There is a 'duck' turtle tracking the duck's location, and so on.
#   The shadow is the point on the perimeter of the pond corresponding
#     to the duck's angular location. This is the point that the wolf
#     always runs toward.

d = Turtle()      # duck's turtle
w = Turtle()      # wolf's turtle
s = Turtle()      # duck's cast shadow turtle

d.hideturtle()
w.hideturtle()
s.hideturtle()

d.speed(0)
w.speed(0)
s.speed(0)

# Graphical drawing accelerators, not used: tracer(0, 0) and update()

s.penup()
s.goto(R*cos(theta), R*sin(theta))
s.pencolor('cyan')
s.dot(14)

w.penup()
w.goto(wx, wy)
w.pencolor('red')
w.dot(10)
w.pendown()


d.penup()
d.goto(R, 0)
d.left(90)
d.pendown()
d.pencolor('blue')
d.circle(R)
d.penup()
d.goto(r1, 0)
d.pendown()
d.pencolor('magenta')
d.circle(r1)
d.penup()
d.goto(r2, 0)
d.pendown()
d.circle(r2)
d.penup()
d.pencolor('green')
d.penup()
d.goto(dx, dy)
d.dot(10)
d.pendown()


def dtr(a): return a*pi/180


def rtd(a): return a*180/pi


def DuckMinusWolfAngle(d_angle, w_angle):
    while d_angle < w_angle - pi: d_angle += 2*pi
    while d_angle > w_angle + pi: d_angle -= 2*pi
    return d_angle, d_angle - w_angle


def DuckCanFlyAway():
    global dr, R, vd, theta, omega
    _, dmw_angle = DuckMinusWolfAngle(theta, omega)
    if (R - dr)/vd < R*dmw_angle/vw: return True
    return False


def NextWolfPosition():
    global omega, theta, w_step, R
    w_angle_step = w_step / R
    w_angle = omega
    d_angle, _ = DuckMinusWolfAngle(theta, omega)
    if d_angle > w_angle:
        if w_angle + w_angle_step >= d_angle: return d_angle
        return w_angle + w_angle_step
    else:
        if w_angle - w_angle_step <= d_angle: return d_angle
        return w_angle - w_angle_step


def Score(x, y):
    global R, r_plateau, theta, omega
    global slope_outer, slope_inner, intercept_outer

    r = sqrt(x**2 + y**2)
    if r < r1:   score = r * slope_inner
    elif r > r2: score = r * slope_outer + intercept_outer
    else:        score = r_plateau

    _, dmw_angle = DuckMinusWolfAngle(atan2(y, x), omega)
    wd_angle = abs(dmw_angle)
    score = score + wd_angle * angle_scale / pi
    return score


def NextDuckPosition(alpha, s):
    global dx, dy
    return dx + s*cos(alpha), dy + s*sin(alpha)


epsilon = 0.1             # for gradient calculation


def GradientDirection():
    global dx, dy, omega, epsilon
    x_grad = Score(dx + epsilon, dy) - Score(dx - epsilon, dy)
    y_grad = Score(dx, dy + epsilon) - Score(dx, dy - epsilon)
    return atan2(y_grad, x_grad)


while True:
    alpha = GradientDirection()
    dx, dy = NextDuckPosition(alpha, d_step)
    theta = atan2(dy, dx)
    dr = sqrt(dx**2 + dy**2)
    omega = NextWolfPosition()
    wx, wy = R*cos(omega), R*sin(omega)

    # Keep theta and omega on [0, 2pi]
    while theta < 0:     theta += 2*pi
    while theta >= 2*pi: theta -= 2*pi
    while omega < 0:     omega += 2*pi
    while omega >= 2*pi: omega -= 2*pi

    print('dmw-angle', round(rtd(theta-omega), 1), '  grad dir:',
          round(rtd(alpha), 1), '  duck r:',
          round(dr, 1), '  score:', round(Score(dx, dy), 3))

    d.goto(dx, dy)
    d.dot(6)
    s.goto(R*cos(theta), R*sin(theta))
    s.dot(10)
    w.goto(wx, wy)
    w.dot(6)

    if DuckCanFlyAway(): break

_, dmw_angle = DuckMinusWolfAngle(theta, omega)
print()
print('The duck can safely swim to the edge of the pond!')
print('  The duck radial location as fraction of R:', dr/R)
print('  The time for the duck to reach shore:', (R - dr)/vd, 'sec')
print('  The time for the wolf to get there:', R*dmw_angle/vw, 'sec')
print()
