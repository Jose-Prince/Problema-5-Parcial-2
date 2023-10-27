# print("Campo Eléctrico para diferentes figuras")


# tortugaxy.setup(600,600)
# tortugaxy.penup()
# tortugaxy.goto(-200,-100)
# tortugaxy.pendown()
# tortugaxy.forward(400)
# tortugaxy.penup()
# tortugaxy.goto(-200,-200)
# tortugaxy.pendown()
# tortugaxy.left(90)
# tortugaxy.forward(400)

import turtle
import tkinter as tk
import pruebas as pr
import Figuras as fig
import CampoElectrico as campo

tortugita = turtle.Turtle()
figura = ""
radio = 0
radioG = 0
radioP = 0
altura = 0
carga = 0
campos = []

def contar_clic():
    global num_clics
    num_clics += 1
    return num_clics

num_clics = 0

def do_stuff():
    tortugita.goto(-600,-600)


def press():
    do_stuff()


def fxn(x, y):
    Celectrico = 0
    tortugator = turtle.Turtle()
    tortugator.hideturtle()
    tortugator.penup()
    tortugator.goto(x, 0)
    tortugator.color("blue")
    if figura == "cono":
        Celectrico = campo.Ccono(float(carga), float(radio),float(altura),  (tortugator.xcor()+300))
    elif figura == "conoT":
        Celectrico = campo.CconoT(float(carga), float(radioG),float(radioP),float(altura),  (tortugator.xcor()+300))
    elif figura == "hemis":
        Celectrico = campo.Chemisferio(float(carga), float(radio),  (tortugator.xcor()+300))
    Celectrico = Celectrico/(10**10)
    tortugator.write("   "+str(contar_clic()))
    CampoElectrico = str("%.2f" % round(Celectrico, 2))+"x10^10 N/C"
    campos.append(CampoElectrico)
    pr.dot(10,tortugator)
    tortugator.pendown()
    fig.flecha(Celectrico, figura,tortugator)
    tortugator.penup()
    
    
# root = tk.Tk()
# canvas = tk.Canvas(root)
# canvas.config(width=900, height=800)
# canvas.pack(side=tk.LEFT)
# screen = turtle.TurtleScreen(canvas)
# screen.bgcolor("cyan")
# button = tk.Button(root, text="Press me", command=press)
# button.pack()
# my_lovely_turtle = turtle.RawTurtle(screen, shape="turtle")
# root.mainloop()

ejecucion = True

positionx = []
positiony = []


while ejecucion:
    figura = print("¿Qué figura desea usar?\n\n1: Cono\n2: Tronco de cono\n3: Hemisferio\n4: Mostrar todas las cordenadas de la carga")
    Opcion = input("Opción: ")
    
    if Opcion == "1":
        figura = "cono"
        radio = input("Radio: ")
        altura = input("Altura: ")
        pr.pantalla()
        fig.cono(float(radio),float(altura),tortugita)
        tortugita.hideturtle()
        carga = float(input("Indique el valor de la carga (C): "))
        print("Vamos a poner la carga por favor seleccionar la posicion de la carga")
        wn = turtle.Turtle()
        wn = turtle.Screen()
        wn.onclick(fxn)
        input()
        
    if Opcion == "2":
        figura = "conoT"
        radioG = input("Radio Mayor: ")
        radioP = input("Radio Menor: ")
        altura = input("Altura: ")
        pr.pantalla()
        fig.conoTruncado(float(radioG),float(radioP),float(altura),tortugita)
        tortugita.hideturtle()
        carga = float(input("Indique el valor de la carga (C): "))
        print("Vamos a poner la carga por favor seleccionar la posicion de la carga")
        wn = turtle.Turtle()
        wn = turtle.Screen()
        wn.onclick(fxn)
        input()
    
    if Opcion == "3":
        figura = "hemis"
        radio = input("Radio: ")
        pr.pantalla()
        fig.hemisferio(float(radio),tortugita)
        tortugita.hideturtle()
        carga = float(input("Indique el valor de la carga (C): "))
        print("Vamos a poner la carga por favor seleccionar la posicion de la carga")
        wn = turtle.Turtle()
        wn = turtle.Screen()
        wn.onclick(fxn)
        input()
    
    



    
    

