import turtle as t
import math

def flower():
    for i in range(360):
        t.forward(math.pi * 2 * 40 / 360)
        t.left((1))
    for i in range(360):
        t.forward(math.pi * 2 * 40 / 360)
        t.right((1))

t.shape("turtle")
t.color("red")
for i in range(3):
    flower()
    t.left(60)

input()