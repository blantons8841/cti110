import turtle

# Set up the screen
screen = turtle.Screen()

# Draw a Square using a for loop
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()

for _ in range(4):
    turtle.forward(50)
    turtle.left(90)

# Draw a Triangle using a for loop
turtle.penup()
turtle.goto(50, 0)
turtle.pendown()

for _ in range(3):
    turtle.forward(50)
    turtle.left(120)

turtle.done()
