#MADE BY SURYA!!

import turtle
import random

screen=turtle.Screen()
screen.bgcolor("black")
screen.title("python Rangoli Maker")

pen=turtle.Turtle()
pen.speed(0)
pen.width(2)

color=["#FF5733","#FFC300","#DAF7A6","#FF33F6","#33FF57","#33D4FF"]

def draw_petal(radius):
    pen.circle(radius,60)
    pen.left(120)
    pen.circle(radius,60)
    pen.left(120)

for i in range(36):
        pen.color(random.choice(color))
        draw_petal(120)
        pen.right(10)

for i in range(18):
    pen.color(random.choice(color))
    for _ in range(4):
        pen.forward(80)
        pen.right(90)
    pen.right(20)

pen.hideturtle()
turtle.done
    
      

