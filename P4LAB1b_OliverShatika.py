import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=500)
turtle.speed(0)
turtle.pensize(3)
turtle.pencolor("purple")

# Draw the Initial 'S'
turtle.penup()
turtle.goto(-60, 30)
turtle.pendown()
turtle.setheading(180)
turtle.circle(15, 180)
turtle.circle(-15, 180)

# Move and Draw the Initial 'O'
turtle.penup()
turtle.goto(30, 0)
turtle.pendown()
turtle.circle(20)

turtle.done()
