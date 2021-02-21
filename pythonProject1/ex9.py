import turtle as t
import math


def fig(n, a):
    t.penup()
    t.goto(0, 0)
    r = a / (2 * math.sin(math.pi / n))
    t.goto(r,0)
    t.left(180-90*(n-2)/n)
    t.pendown()
    for i in range(n):
        t.forward(a)
        t.left(180-180*(n-2)/n)
    t.right(180 - 90*(n-2)/n)

t.shape("turtle")
t.color("red")
for i in range(3, 14, 1):
    fig(i, 20*i)

input()
