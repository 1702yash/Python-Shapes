import turtle

t = turtle.Turtle()
t.speed(0)

# Face
t.penup()
t.goto(0, -100)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

# Left eye
t.penup()
t.goto(-40, 30)
t.pendown()
t.dot(15)

# Right eye
t.penup()
t.goto(40, 30)
t.pendown()
t.dot(15)

# Smile
t.penup()
t.goto(-40, -20)
t.setheading(-60)
t.pendown()
t.circle(50, 120)

turtle.done()