import turtle as t
import math

t.shape("turtle")
t.color("red")
t.speed = 0
t.goto(0, 0)


def num(a):
    t.penup()
    for i in range(2):
        t.right(a[2 * i])
        t.forward(a[2 * i + 1])
    for i in range(2, len(a) // 2):
        t.pendown()
        t.forward(a[2 * i])
        t.right(a[2 * i + 1])
    another()


def another():
    t.penup()
    t.right(90)
    t.forward(15)
    t.pendown()


a1 = (90, 30, 225, 0, 30 * math.sqrt(2), 135, 60, 180, 60, 0)
a4 = (0, 0, 90, 0, 30, 270, 30, 90, 30, 180, 60, 0)
a7 = (0, 0, 0, 0, 30, 135, 30 * math.sqrt(2), 315, 30, 180, 30, 45, 30* math.sqrt(2), 315)
a0 = (0, 0, 90, 0, 60, 270, 30, 270, 60, 270, 30, 180, 30, 270)

num(a1)
num(a4)
num(a1)
num(a7)
num(a0)
num(a0)
