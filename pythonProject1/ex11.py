import turtle as t
import math

def rond(r):
    for i in range(360):
        t.forward(math.pi * 2 * r / 360)
        t.left((1))
    for i in range(360):
        t.forward(math.pi * 2 * r / 360)
        t.right((1))


t.shape("turtle")
t.color("red")
t.left(90)
t.speed(50)
for i in range(3):
    rond(30 + 5*i)

input()