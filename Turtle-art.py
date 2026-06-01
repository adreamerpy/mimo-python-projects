import turtle
import colorsys

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.width(2)

# Color and Drawing Loop
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
    t.forward(i * 0.5)
    t.right(144)
    h += 0.005

t.hideturtle()
turtle.done()