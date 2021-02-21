import turtle as t

t.shape("turtle")
t.color("green")
for i in range(1, 11, 1):
    t.penup()
    t.goto(0, 0)
    t.right(90)
    t.forward((5*i))
    t.right(90)
    t.forward((5*i))
    t.pendown()
    t.right(90)
    t.right(90)
    t.forward(10*i)
    t.left(90)
    t.forward(10*i)
    t.left(90)
    t.forward(10*i)
    t.left(90)
    t.forward(10*i)

input()
