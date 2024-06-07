#Lienzo qu integre movimiento de personajes (Imagen - Sprits)
import tkinter as tk
from PIL import Image, ImageTk #pip install pillow

#Crear una clase que maneje el Lienzo
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #Configuracion de la ventana
        self.title("Juego Perzonaje")
        self.canvas=tk.Canvas(self, width=800, height=600, bg='white')
        self.canvas.pack()

        #Cargar y Redimensionar la imagen de Fondo
        self.imagen_fondo=Image.open("fondo.jpg")
        self.imagen_fondo=self.imagen_fondo.resize((800,600),Image.Resampling.LANCZOS)
        self.imagen_fondo_juego=ImageTk.PhotoImage(self.imagen_fondo)
        self.canvas.create_image(400,300, image=self.imagen_fondo_juego)




        #Configuracion del personaje
        self.imagen=Image.open("personaje.png")
        self.imagen=self.imagen.resize((50,50),Image.Resampling.LANCZOS)
        self.personaje_Imagen=ImageTk.PhotoImage(self.imagen)

        #Crear un objeto de la imagen en el lienzo
        self.personaje=self.canvas.create_image(400,300, image=self.personaje_Imagen)

        #Cargar y redimensionar el bloque de colision
        self.imagen_bloque=Image.open("bloque.png")
        self.imagen_bloque=self.imagen_bloque.resize((50,50),Image.Resampling.LANCZOS)
        self.imagen_bloque_juego=ImageTk.PhotoImage(self.imagen_bloque)

        #crear varios bloques de colision
        self.bloques=[
            self.canvas.create_image(200,200, image=self.imagen_bloque_juego),
            self.canvas.create_image(300,300, image=self.imagen_bloque_juego),
            self.canvas.create_image(500,500, image=self.imagen_bloque_juego)
        ]




        #Vincular las teclas con  la funcion del movimiento
        self.bind("<KeyPress>",self.click)


    #CONFIGURAR LAS ACCIONES DE LA CLASE
    def click(self,evento):
        tecla=evento.keysym
        x=0
        y=0

        #Configurar una condicional para el manejo del personaje con el teclado
        if tecla=="Left":
            x=-10
        elif tecla=="Right":
            x=10
        elif tecla=="Up":
            y=-10
        elif tecla=="Down":
            y=10
        #Mover el personaje si no colisiona con los bloques
        if not self.colision(self.personaje,x,y):
            self.canvas.move(self.personaje,x,y)
    
    def colision(self,personaje, dx, dy):
        #Obtener las coordenas del personaje
        coordenadas_personaje=self.canvas.coords(personaje)
        #calcular las nuevas coordenadas despues del movimiento
        nuevas_coordenadas=[coordenadas_personaje[0]+dx,coordenadas_personaje[1]+dy]

        for bloque in self.bloques:
            coordenasdas_bloques=self.canvas.coords(bloque)
            #verificar si las nuevas coordenadas del personaje colisionan con alguno de los bloques
            if abs(nuevas_coordenadas[0]-coordenasdas_bloques[0])<50 and abs(nuevas_coordenadas[1]-coordenasdas_bloques[1])<50:
                return True
        return False

        #MOVEER EL PERSONAJE EN EL LIENZO
        #self.canvas.move(self.personaje,x , y)

#Crear la funcion principal
if __name__=="__main__":
    juego=App()
    juego.mainloop()
            
