import turtle as t

t.shape("turtle")
t.color("red")
n = 12
t.penup()
t.goto(0, 0)
t.pendown()
t.stamp()
for i in range(n):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.forward((100))
    t.stamp()
    t.left(360/n)


input()
