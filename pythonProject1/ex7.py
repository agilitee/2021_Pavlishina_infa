import turtle as t
import math

k = 0.00005
t.shape("turtle")
t.color("red")
t.penup()
t.goto(0, 0)
t.pendown()
for i in range(2000):
  t.forward(k*i*2*math.pi)
  t.left((1))

input()