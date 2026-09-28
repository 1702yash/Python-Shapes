# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 07:01:42 2026

@author: User
"""

import turtle 
t = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor("skyblue")



# Grass

t.penup()
t.goto(-400,-200)
t.pendown()


t.fillcolor("lightgreen")
t.begin_fill()
t.goto(400,-200)
t.goto(400,-400)
t.goto(-400,-400)
t.goto(-400,-200)
t.end_fill()


t.penup()
t.goto(0,0)
t.pendown()



# Mountains
t.penup()
t.left(180)
t.forward(200)
t.right(90)
t.forward(150)
t.right(90)
t.pendown()

t.fillcolor("sienna")
t.begin_fill()


t.left(60)
t.forward(150)
t.right(120)
t.forward(150)
t.left(120)
t.forward(150)
t.right(120)
t.forward(150)
t.left(120)
t.forward(150)
t.right(120)
t.forward(150)

t.end_fill()


# Sun
t.penup()
t.right(180)
t.forward(150)
t.left(120)
t.forward(25)
t.right(90) 
t.pendown()
t.fillcolor("gold")
t.begin_fill()
t.circle(125,60)
t.end_fill()


# Hut's Triangle with Circle
t.penup()
t.goto(-300,-50)
t.left(150)
t.pendown()


t.fillcolor("sienna")
t.begin_fill()

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.end_fill()

t.penup()
t.left(120)
t.forward(50)
t.left(90)
t.forward(10)
t.right(90)
t.pendown()

t.fillcolor("skyblue")
t.begin_fill()
t.circle(18)
t.end_fill()


# Hut's Para
t.penup()
t.goto(-200,-50)
t.pendown()

t.fillcolor("sienna")
t.begin_fill()

t.forward(200)
t.left(120)
t.forward(100)
t.left(60)
t.forward(200)
t.end_fill()


# Hut's Front
t.penup()
t.goto(-300,-50)
t.pendown()

t.fillcolor("grey")
t.begin_fill()

t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)



# Hut's Back
t.penup()
t.left(180)
t.forward(150)
t.pendown()

t.left(90)
t.forward(200)
t.left(90)
t.forward(150)
t.end_fill()


# Hut's Back Window
t.penup()
t.goto(-70,-130)
t.pendown()


t.fillcolor("skyblue")
t.begin_fill()

t.forward(50)
t.left(90)
t.forward(80)
t.left(90)
t.forward(50)
t.left(90)
t.forward(80)
t.left(90)
t.end_fill()



t.penup()
t.forward(25)
t.pendown()
t.left(90)
t.forward(80)
t.right(90)
t.penup()
t.goto(-110,-130)
t.pendown()
t.forward(50)



# Door
t.penup()
t.goto(-275,-200)
t.pendown()

t.fillcolor("saddlebrown")
t.begin_fill()
t.forward(75)
t.right(90)
t.forward(50)
t.right(90)
t.forward(75)
t.end_fill()



# Door's Handle
t.penup()
t.goto(-270,-170)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.circle(2)
t.end_fill()






# Tree
t.penup()
t.goto(130,-200)
t.pendown()

t.fillcolor("saddlebrown")
t.begin_fill()
t.left(90)
t.circle(75,180)


t.penup()
t.goto(300,-50)
t.pendown()
t.circle(75,180)

t.end_fill()


t.penup()
t.goto(235,-90)
t.pendown()

t.fillcolor("green")
t.begin_fill()
t.right(40)
t.circle(50,180)
t.right(120)
t.circle(50,180)
t.right(120)
t.circle(50,180)
t.right(120)
t.circle(50,180)
t.right(120)
t.circle(50,180)
t.right(90)
t.circle(50,90)
t.end_fill()





# Sunsine
t.penup()
t.goto(60,270)
t.pendown()
t.left(90)
t.forward(15)

t.penup()
t.goto(100,275)
t.pendown()
t.right(20)
t.forward(15)

t.penup()
t.goto(140,270)
t.pendown()
t.right(20)
t.forward(15)




# Sun color

t.penup()
t.goto(163,258)
t.pendown()


t.fillcolor("gold")
t.begin_fill()
t.right(190)
t.forward(125)
t.right(120)
t.forward(125)    
t.end_fill()








# Fruits

t.penup()
t.goto(110,-10)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(130,-40)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(120,50)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(150,30)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(160,-18)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(200,20)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(220,-10)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(170,-50)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(210,-70)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(250,-40)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(280,-10)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(260,30)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(300,10)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(240,70)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(220,110)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(170,70)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(10)
t.end_fill()







