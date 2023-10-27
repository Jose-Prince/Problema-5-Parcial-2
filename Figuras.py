from turtle import *
import tkinter as tk
import math

# for _ in range(3):
#     t.forward(100)  # Length of each side
#     t.left(120)     # Turn 120 degrees to form an equilateral triangle

def cono(radio, altura, t):#t es tortuga
    t.penup()
    t.goto(-300,-radio)
    t.pendown()
    hipotenusa = math.hypot(radio,altura)
    angulo = math.atan(altura/radio)
    angulo = math.degrees(angulo)
    angulo2 = math.atan(radio/altura)
    angulo2 = math.degrees(angulo2)
    t.left(90-angulo)    
    t.forward(hipotenusa)
    t.right(180)
    t.right(2*angulo2)
    t.forward(hipotenusa)
    t.penup()
    t.goto(-300,-radio)
    t.pendown()
    ovalo(radio,t)
    orPos(t)

def conoTruncado(radio2,radio1,altura, t): #radio 2 es grande y radio 1 es peque
    t.penup()
    t.goto(-300,-radio2)
    t.pendown()
    ovalo(radio2,t)
    hipotenusa = math.hypot(radio2-radio1,altura)
    angulo = math.atan(altura/(radio2-radio1))
    angulo = math.degrees(angulo)
    angulo2 = math.atan((radio2-radio1)/altura)
    angulo2 = math.degrees(angulo2)
    t.left(90-angulo)    
    t.forward(hipotenusa)
    ovalo2(radio1,t)
    t.setheading(0)
    t.right(180+angulo2)
    t.forward(hipotenusa)
    orPos(t)

def hemisferio(radio, t):
    t.penup()
    t.goto(-300,radio)
    t.pendown()
    t.setheading(180)
    t.circle(radio,180)
    t.penup()
    t.goto(-300,-radio)
    t.pendown()
    ovalo(radio,t)
    orPos(t)
        
def ovalo(radio,t):
    t.setheading(0)
    t.left(45)
    t.circle(radio*1.43,90)
    t.left(90)
    t.circle(radio*1.43,90)
    t.setheading(0)
    
def ovalo2(radio,t):
    t.setheading(0)
    t.left(45)
    t.circle(radio*1.43,90)
    
def orPos(t):
    t.penup()
    t.goto(-300,0)
    t.setheading(0)
    
def flecha(CampoElectrico,figura,t):
    t.pensize(3)
    if figura == "Cono" or figura == "Tronco de Cono":
        t.forward(CampoElectrico*500)
        
    else:
        t.forward(CampoElectrico*50)
    if CampoElectrico > 0:
        t.left(90)
        t.forward(10)
        
        t.right(90+19)
        t.forward(30)
        
        t.penup()
        t.setheading(0)
        t.backward(28.4)
        t.pendown()
        t.right(90)
        t.forward(10)
        
        t.left(90+19)
        t.forward(30)
        t.setheading(0)
    else:
        t.setheading(180)
        t.left(90)
        t.forward(10)
        
        t.right(90+19)
        t.forward(30)
        
        t.penup()
        t.setheading(180)
        t.backward(28.4)
        t.pendown()
        t.right(90)
        t.forward(10)
        
        t.left(90+19)
        t.forward(30)
        t.setheading(0)
        
        
    
    
    