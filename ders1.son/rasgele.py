import turtle
import random


for x in range(10):
    turtle.up()
    turtle.goto(random.randint(-200,200),random.randint(-200,200))
    turtle.down()
    ku = random.randint(30,100)
    for aa in range(4):
        turtle.forward(ku)
        turtle.right(90)

input()

