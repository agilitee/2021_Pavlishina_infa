import turtle as t

t.shape("turtle")
t.color("red")
t.penup()
t.goto(0, 0)
t.pendown()
for i in range(20):
    t.forward(5+5*i)
    t.left(90)

input()