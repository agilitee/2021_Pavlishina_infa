import turtle as t
import math

t.shape("turtle")
t.color("red")
t.penup()
t.goto(0, 0)
t.forward((40))
t.left(90)
t.pendown()
for i in range(360):
  t.forward(math.pi*2*40/360)
  t.left((1))

input()