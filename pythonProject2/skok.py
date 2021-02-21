import turtle as t

t.shape("turtle")
t.penup()
t.goto(0, 0)
t.pendown()
x = 0.01
y = 0.01
vx = 10
vy = 40
ay = -10
dt = 0.1
t.speed = 30
while True:
    if y > 0:
        x += vx * dt
        vy += ay * dt
        y += vy * dt + ay * dt ** 2 / 2
        t.goto(x, y)
    elif y == 0:
        y = 0.1
        t.goto(x, y)
        vy = -0.9 * vy
        vx = 0.9 * vx
    elif y < 0:
        y = 0.1
        t.goto(x, y)
        vy = -0.9 * vy
        vx = 0.9 * vx