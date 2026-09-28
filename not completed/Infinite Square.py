
import turtle
t = turtle.Turtle()

t.penup()
t.goto(-250,-250)
t.pendown()


a=500

for i in range(2):
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.left(90)
    t.penup()
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.pendown()
    
    
    