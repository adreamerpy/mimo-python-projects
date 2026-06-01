import turtle
import colorsys

# Setup the screen
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0) # Fastest speed
n = 36
h = 0

# Drawing the spiral pattern
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
    h += 1/n
    t.forward(i * 2 / 3 + i)
    t.left(10)
    t.forward(i)
    t.left(121)

turtle.done()