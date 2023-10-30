import turtle
import tkinter as tk
import math

##plano
def plano(densidad, plano):
    
    plano.width(3)
    plano.fillcolor("#ff6600")
    
    plano.penup()
    plano.goto(0,-100)
    plano.left(45)
    plano.pendown()
    plano.begin_fill()
    plano.back(150)
    plano.forward(300)
    plano.left(45)
    plano.forward(200)
    plano.right(45)
    plano.back(300)
    plano.left(45)
    plano.back(200)
    plano.end_fill()
    plano.penup()
    plano.goto(0,0)
    plano.goto(0,25)
    plano.write("Densidad lineal:" + str(densidad) +"C/m")
    plano.goto(0,0)
    plano.pendown()
    plano.width(1)
    plano.goto(200,0)
    plano.hideturtle()
    plano.seth(0)

   
def fparticula(totald, part, color):

    part.color(str(color))
    part.shapesize(stretch_wid=0.25, stretch_len=0.25, outline=0.5)

    progress(int(totald), part)
    part.right(180)
    progress(int(totald), part)


def fparticulaesf(totald, part, color, radio):

    part.color(str(color))
    part.shapesize(stretch_wid=0.25, stretch_len=0.25, outline=0.5)

    if(totald > radio):
        progress(int(totald), part)
    
    else:
        progress(int(totald), part)
        part.right(180)
        progress(int(totald), part)


def progress(totald, tortuga):
    
    i = 0
    p = 0
    while(i < (totald-(totald/5))):
        i = i + (totald/20)
        if((p % 2) == 0):
            tortuga.forward(totald/5)
        else:
            tortuga.penup()
            tortuga.forward(totald/5)
            tortuga.pendown()
        p = p +1
    tortuga.forward(totald-i)



##Esfera

def esfera(radio, part):
    part.width(3)
    part.right(90)
    part.penup()
    part.forward(radio)
    part.left(90)
    part.pendown()
    part.circle(radio)
    part.circle(radio, -70)
    part.right(-45)
    part.penup()
    part.forward(radio/8)
    part.right(45)
    part.forward(radio/15)
    part.left(10)
    part.seth(-43)
    part.pendown()
    
    


# rad --> radius of arc
    for i in range(2):
        
        # two arcs
        part.circle(radio*1.17,90)
        part.circle(radio*1.17//2,90)
            # Main section
    # tilt the shape to negative 45

    part.penup()
    part.goto(0,0)
    part.right(90)
    part.forward(radio)
    part.left(90)
    part.circle(radio)
    part.circle(radio, 70)
    part.right(-45)
    part.penup()
    part.forward(radio/9)
    part.right(45)
    part.forward(-radio/8)
    part.left(10)
    part.seth(43)
    part.pendown()
    
    


# rad --> radius of arc
    for i in range(2):
        
        # two arcs
        part.circle(radio*1.17,90)
        part.circle(radio*1.17//2,90)
 

 

    


