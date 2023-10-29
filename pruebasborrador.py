import turtle
from turtle import RawTurtle, ScrolledCanvas
import tkinter as tk
import Figuras as figure
import Funciones as func

class esfera:
    def __init__(self, radio, carga, cargaparticula, masa, rapidez):
        self.radio = radio
        self.carga = carga
        self.masa = masa
        self.cargaparticula = cargaparticula
        self.rapidez = rapidez


class plano:
    def __init__(self, densidad,cargaparticula, masa, rapidez):
        self.densidad = densidad
        self.masa = masa
        self.cargaparticula = cargaparticula
        self.rapidez = rapidez

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
    tortuga.forward(screensize)
    tortuga.write("x+")
    tortuga.goto(0,0)

def ybar(tortuga,screensize):
    tortuga.penup()
    tortuga.goto(0,0)
    tortuga.pendown()
    tortuga.left(90)
    tortuga.backward(screensize-40)
    tortuga.forward((screensize-40)*2)
    tortuga.right(90)
    tortuga.write("y+")
    tortuga.goto(0,0)

def zbar(tortuga,screensize):
    tortuga.penup()
    tortuga.goto(0,0)
    tortuga.pendown()
    tortuga.left(45)
    tortuga.backward((screensize-90))
    tortuga.forward((screensize-90)*2)
    tortuga.right(45)
    tortuga.write("z+")
    tortuga.goto(0,0)

def dot(size,t):
    t.color("red")
    t.dot(size)


def pantalla():
    # Set up the screen
    tortugagrid = turtle.RawTurtle(screen, shape="arrow")
    tortugagrid._tracer(False)
    tortugagrid.color("#D3D3D3")
    screensize = 300
    actualscreen = 800 #resolucion de la pantalla

    draw_grid(step=10, size = actualscreen, turtle=tortugagrid), 

    tortugagrid._tracer(True)
    tortugagrid.color("black")
    tortugagrid.shapesize(0.25,0.5,0.5)
    tortugagrid.speed(0)
    mainpos(tortugagrid,screensize)
    xbar(tortugagrid,screensize)
    ybar(tortugagrid,screensize)
    zbar(tortugagrid,screensize)

def check_button_command(entrycargaesfera):
    
    if (esfera.get() == 1 and plano.get() == 0):
        datos.config(text="Se selecciono la esfera")
        dato1.config(text="Escribir el radio (m)")
        dato1.grid(row=5,column=0)
        entryradio.grid(row=6,column=0)
        dato2.config(text="Escribir la carga negativa (C)")
        dato2.grid(row=7,column=0)
        entrycargaesfera.grid(row=8,column=0)
        
        


    if (plano.get() == 2 and esfera.get() == 0):
        
        dato2.grid_remove()
        entrycargaesfera.grid_remove()
        entryradio.grid_remove()
        datos.config(text="Se selecciono el plano infinito")
        dato1.config(text="Escribir la densidad superficial de carga (C/m)")
        dato1.grid(row=5,column=0)
        entrydens.grid(row=6,column=0)
    
    if ((plano.get() == 0 and esfera.get() == 0) or (plano.get() == 2 and esfera.get() == 1 )):
        datos.config(text="Esperando la selección de la carga central....")
        dato1.grid_remove()
        dato2.grid_remove()
        entrycargaesfera.grid_remove()
        entryradio.grid_remove()
        entrydens.grid_remove()

        

def meterdatos(cond, carga,masa,rapidez, radio,cargaesfera,densidad, particula, esfera, plano):
    #plano
    if(plano == 2):
        rapi.config(text="Ingrese la rapidez inicial")

        if((int(rapidez) > 300000000)):
            rapidez = 300000000
            rapi.config(text="Ilegalidad: cantidad mayor a la velocidad de la luz\n Se ha puesto por default 3*10^8 m/s")

        cplano.cargaparticula = int(carga)
        cplano.densidad = int(densidad)
        cplano.masa = int(masa)
        cplano.rapidez = int(rapidez)

        distanciap = func.distanceP(rapidez, densidad, dicprotones[particula], dicneutrones[particula])
        figure.plano(densidad, planos)
        part = turtle.RawTurtle(screen, shape="circle")
        figure.fparticula(int(distanciap), part, color="blue")

        


    #esfera
    if(esfera == 1):
        cesfera.cargaparticula = carga
        cesfera.cargaparticula =  cargaesfera
        cesfera.radio = radio
        cplano.masa = masa
        cplano.rapidez = rapidez
        func.distanceS( int(radio), dicprotones[particula], dicneutrones[particula], int(rapidez))

    



if __name__ == "__main__":

    global cesfera
    cesfera = esfera(radio=1, carga=1, cargaparticula=1, masa=1, rapidez=1)
    global cplano
    cplano = plano(densidad= 1, cargaparticula=1,masa=1, rapidez= 1)
    fig = 0
    
    
    dicprotones = {
    "Protones": 1,
    "Positrones": 1,
    "Berilio-8": 4,
    "Helio-4": 2,
    "Alfa triplemente cargada": 2,
    "Núcleo de carbono" : 6,
    "Núcleo de oxígeno" : 8

    }
    
    dicneutrones = {
    "Protones": 1,
    "Positrones": 1,
    "Berilio-8": 4,
    "Helio-4": 2,
    "Alfa triplemente cargada": 1,
    "Núcleo de carbono" : 6,
    "Núcleo de oxígeno" : 8

    }
   
    
    root = tk.Tk()
    plano = tk.IntVar()
    esfera = tk.IntVar()
    names = ["Protones", "Positrones", "Berilio-8", "Helio-4", "Alfa triplemente cargada", "Núcleo de carbono", "Núcleo de oxígeno"]

    particula = tk.StringVar()
    particula.set(names[0])
## Helio-4, que consta de dos protones y dos neutrones
##Alfa triplemente cargada: compone de dos protones y un neutrón y tiene una carga eléctrica de +3e
## El berilio-8 es un núcleo inestable compuesto por cuatro protones y cuatro neutrones.
    entryradio = tk.Entry(root)
    entrycargaesfera = tk.Entry(root)
    entrydens = tk.Entry(root)

    
    canvas = tk.Canvas(root)
    canvas.config(width=800, height=600)
    canvas.grid(row=1,column=1,rowspan=40, columnspan=2 )
    screen = turtle.TurtleScreen(canvas)
    planos = turtle.RawTurtle(screen, shape="arrow")
    pantalla()
    tk.Label(root, text="Calculo de velocidad de una párticula", font=("Arial", 16)).grid(row=0,column=1, columnspan=2)
    tk.Label(root, text="Seleccione el tipo de carga central fija", font=("Arial", 12)).grid(row=1,column=0)
    c1 = tk.Checkbutton(root, text='Esfera',variable=esfera, onvalue=1, offvalue=0, font=("Arial", 10), command= lambda: check_button_command(entrycargaesfera) ).grid(row=2,column=0)
    c2 = tk.Checkbutton(root, text='Plano',variable=plano, onvalue=2, command= lambda: check_button_command(entrycargaesfera),offvalue=0, font=("Arial", 10) ).grid(row=3, column=0)
    
    

    datos = tk.Label(root, text="Esperando la selección de la carga central....", font=("Arial", 8))
    datos.grid(row=4,column=0)    

    dato1 = tk.Label(root, font=("Arial", 10))
    dato1.grid(row=5,column=0)
    dato2 = tk.Label(root)
    dato2.grid(row=7,column=0)
   
    


    tk.Label(root, text="Seleccione la partícula que quiera disparar", font=("Arial", 12)).grid(row=10,column=0)
    tk.OptionMenu(root, particula ,*names).grid(row=11, column=0)
    #nombrepart = particula.get()
    tk.Label(root, text="Datos Importantes", font=("Arial", 12)).grid(row=22,column=0)
    tk.Label(root, text="Ingrese la carga", font=("Arial", 12)).grid(row=23,column=0)
    entrycargapart = tk.Entry(root)
    entrycargapart.grid(row=24, column=0)
    tk.Label(root, text="Ingrese la masa", font=("Arial", 12)).grid(row=25,column=0)
    masa = tk.Entry(root)
    masa.grid(row=26,column=0)
    rapi = tk.Label(root, text="Ingrese la rapidez inicial", font=("Arial", 12))
    rapi.grid(row=27,column=0)
    rapidez = tk.Entry(root)
    rapidez.grid(row=28, column=0)
    

    submit = tk.Button(root, text="Generar Resultados...", command= lambda: meterdatos(fig, entrycargapart.get(),masa.get(), rapidez.get(),entryradio.get(),entrycargaesfera.get(),entrydens.get(), particula.get(), esfera.get(), plano.get() ))
    submit.grid(row=29,column=0)

    velo = tk.Label(root, text="Rapidez inicial: " + str(0) + "m/s", font=("Arial", 12))
    velo.grid(row=41,column=1)

    dist = tk.Label(root, text="Distancia de máximo alejamiento: " + str(0) + "metros", font=("Arial", 12))
    dist.grid(row=41,column=2)

    root.mainloop()