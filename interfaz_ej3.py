#Juego para atrapar la pelotita
import tkinter as tk
import random

#Clase Principal Atrapar la Pelota
class AtrapaPelota:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Atrapa la pelotita")
        self.canvas_Ancho=600
        self.canvas_Alto=400

        self.canvas=tk.Canvas(ventana,width=self.canvas_Ancho, height=self.canvas_Alto, bg="white")
        self.canvas.pack()

        #Objetos
        self.personaje_tamaño=50
        self.pelota_tamaño=30

        self.personaje=self.canvas.create_rectangle(0,0,self.personaje_tamaño,self.personaje_tamaño, fill="blue")
        self.pelota=self.canvas.create_oval(0,0,self.pelota_tamaño,self.pelota_tamaño, fill="red")

        self.canvas.move(self.personaje,275,175)

        self.moverCirculo()
        self.ventana.bind("<Left>",self.moverIzquierda)
        self.ventana.bind("<Right>",self.moverDerecha)
        self.ventana.bind("<Up>",self.moverArriba)
        self.ventana.bind("<Down>",self.moverAbajo)

    #METODOS O ACCIONES DE LA CLASE
    def moverCirculo(self):
        self.canvas.move(self.pelota,random.randint(1,self.canvas_Ancho-self.pelota_tamaño),random.randint(1,self.canvas_Alto-self.pelota_tamaño))
        self.ventana.after(1000,self.moverCirculo)
    
    def moverIzquierda(self,evento):
        self.canvas.move(self.personaje,-20,0)
    
    def moverDerecha(self,evento):
        self.canvas.move(self.personaje,20,0)
    
    def moverArriba(self,evento):
        self.canvas.move(self.personaje,0,-20)
    
    def moverAbajo(self,evento):
        self.canvas.move(self.personaje,0,20)
    
    def colision(self):
        personaje_coordenadas=self.canvas.coords(self.personaje)
        pelota_coordenadas=self.canvas.coords(self.pelota)

        if (personaje_coordenadas[2]>pelota_coordenadas[0] and personaje_coordenadas[0]<pelota_coordenadas[2] and personaje_coordenadas[3]>pelota_coordenadas[1] and personaje_coordenadas[1]<pelota_coordenadas[3]):
            self.canvas.itemconfig(self.pelota, fill="green")
        else:
            self.canvas.itemconfig(self.pelota, fill="red")

        self.ventana.after(50,self.colision)


ventana=tk.Tk()
juego=AtrapaPelota(ventana)

ventana.mainloop()