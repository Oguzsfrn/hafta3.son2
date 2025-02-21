import turtle
import random

t = turtle.Turtle()
t.speed(0)
# Kodunuzu buraya yazınız
i = 0

while True:
    kirmizi = random.randint(0,255)
    yesil = random.randint(0,255)
    mavi = random.randint(0,255)
    t.forward(i)
    t.right(90)
    i = i + 5

input()