import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Aesthetic Animation")

# Ball setup
ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.penup()

# List of colors
colors = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "magenta"]

# Movement
dx = 5
dy = 5

while True:
    ball.forward(dx)
    ball.right(1)
    
    # Change color on wall collision
    if ball.xcor() > 200 or ball.xcor() < -200:
        dx *= -1
        ball.color(random.choice(colors))
    if ball.ycor() > 200 or ball.ycor() < -200:
        dy *= -1
        ball.color(random.choice(colors))