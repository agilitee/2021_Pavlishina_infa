import random as r
import turtle as t

t.shape("turtle")
t.color("red")
t.speed(50)
for i in range(100):
    t.forward(r.randint(1, 60))
    t.left(r.randint(1, 360))

input()
