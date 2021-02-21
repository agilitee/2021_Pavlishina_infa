import turtle as t
import math

def rond(r):
    for i in range(360):
        t.forward(math.pi * 2 * r / 360)
        t.left((1))

t.speed(1000000)
t.shape("turtle")
t.penup()
t.goto(100, 0)
t.left(90)
t.pendown()

t.begin_fill()
rond(100)
t.color("yellow")
t.end_fill()

t.penup()
t.goto(-45, 45)
t.right(1)
t.pendown()
t.begin_fill()
rond(10)
t.color("blue")
t.end_fill()

t.penup()
t.goto(45, 45)
t.right(1)
t.pendown()
t.begin_fill()
rond(10)
t.color("blue")
t.end_fill()

t.penup()
t.goto(0, 40)
t.right(1)
t.right(180)
t.pendown()
t.width(5)
t.color("black")
t.forward(10)

t.penup()
t.goto(-50, 10)
t.pendown()
t.width(5)
t.color("red")
for i in range(180):
    t.forward(math.pi * 2 * 50 / 360)
    t.left((1))

input()