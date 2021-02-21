import turtle as t
import math

def pr():
    for i in range(180):
        t.forward(math.pi * 2 * 40 / 360)
        t.left((1))
    for i in range(180):
        t.forward(math.pi * 2 * 5 / 360)
        t.left((1))

t.shape("turtle")
t.color("red")
t.left(90)
for i in range(4):
    t.speed(100)
    pr()

input()