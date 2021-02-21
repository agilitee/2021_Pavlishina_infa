import turtle as t
import math

def star(n, a):
    t.penup()
    t.goto(0, 0)
    r = a / (2 * math.sin(math.pi / n))
    t.goto(r, 0)
    t.left(180/n + 90)
    t.pendown()
    for i in range(n):
        t.forward(a)
        t.left(180-180/n)
    t.right(180-180/n)

t.shape("turtle")
star(5,40)
star(11, 40)

input()
