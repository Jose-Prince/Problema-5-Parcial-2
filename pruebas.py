import turtle
from turtle import RawTurtle, ScrolledCanvas
import tkinter as tk

def draw_grid(step, size,turtle):
    for i in range(-size, (size+1), step):
        turtle.penup()
        turtle.goto(i, -size)
        turtle.pendown()
        turtle.goto(i, size)
        
    for i in range(-size, (size+1), step):
        turtle.penup()
        turtle.goto(-size, i)
        turtle.pendown()
        turtle.goto(size, i)


def mainpos(tortuga,screensize):
    tortuga.penup()
    tortuga.goto(-screensize,0)
    tortuga.pendown()

def xbar(tortuga,screensize):
    tortuga.penup()
    tortuga.goto(-screensize,0)
    tortuga.pendown()
    tortuga.back(-screensize)
    tortuga.forward(screensize-20)
    tortuga.write("x+")
    tortuga.goto(-screensize,0)

def ybar(tortuga,screensize):
    tortuga.penup()
    tortuga.goto(-screensize,0)
    tortuga.pendown()
    tortuga.left(90)
    tortuga.backward(screensize-90)
    tortuga.forward((screensize-90)*2)
    tortuga.right(90)
    tortuga.write("y+")
    tortuga.goto(-screensize,0)

def dot(size,t):
    t.color("red")
    t.dot(size)


def pantalla():
    # Set up the screen
    turtle.Turtle()
    turtle.tracer(False)
    turtle.update()
    turtle.color("#D3D3D3")
    screensize = 300
    actualscreen = 800 #resolucion de la pantalla

    draw_grid(step=10, size = actualscreen, turtle=turtle), 

    turtle.tracer(True)
    turtle.update()

    tortugagrid = turtle.Turtle()
    tortugagrid.shape("arrow")
    tortugagrid.color("blue")
    tortugagrid.shapesize(0.25,0.5,0.5)
    tortugagrid.speed(0)
    mainpos(tortugagrid,screensize)
    xbar(tortugagrid,screensize)
    ybar(tortugagrid,screensize)
