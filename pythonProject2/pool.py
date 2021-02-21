from random import randint
import turtle


number_of_turtles = 60
steps_of_time_number = 100


pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-300, 300), randint(-300, 300))


for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(randint(3,7))
        unit.left(randint(1,360))
        unit.forward(randint(3,7))