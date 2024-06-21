#Ejercicio de desarrollo de una galeria de imagenes que permita:
#Navegar por las imagenes, que se pueda abrir la carpeta con el archivo tipo imagen
#Proporcionar opciones para cambiar de imagenes

#Paso 1. Importar las librerias necesarias
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image,ImageTk
import os

#Paso 2. Crear la clase principal de la aplicacion
class Galeria:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Galeria de Imagenes")
        self.ventana.geometry("700x500")

        #Paso 3. Incializar las variables
        self.lista_imagenes=[]
        self.imagen_id_abrir=0
        self.abrir_imagen=None

        #Paso 4. Crear la interfaz
        self.crear_Interfaz()

    #Metodo o accion de la clase
    def crear_Interfaz(self):
        #Crear pantallas(frames) para la imagen
        self.frame_imagen=ttk.Frame(self.ventana)
        self.frame_imagen.pack(padx=10,pady=10)

        self.label_imagen=ttk.Label(self.frame_imagen,text="Seleccione una carperta para ver las imagenes")
        self.label_imagen.pack()
        #Botones de navegacion
        self.frame_botones=ttk.Frame(self.ventana)
        self.frame_botones.pack(pady=10)

        #Crear los botones
        self.boton_anterior=ttk.Button(self.frame_botones,text="<< Anterior", command=self.imagenAnterior)
        self.boton_anterior.pack(side=tk.LEFT, padx=10)

        self.boton_siguiente=ttk.Button(self.frame_botones,text="Siguiente >>",command=self.imagenSiguiente)
        self.boton_siguiente.pack(side=tk.LEFT,padx=10)

        #Menu
        self.crear_menu()

    def crear_menu(self):
        menu_superior=tk.Menu(self.ventana)
        self.ventana.config(menu=menu_superior)
        archivo_menu=tk.Menu(menu_superior,tearoff=0)
        menu_superior.add_cascade(label="Archivo",menu=archivo_menu)

        archivo_menu.add_command(label="Abrir Carpeta", command=self.abrir_archivo)
        menu_superior.add_separator()

        archivo_menu.add_command(label="Salir",command=self.ventana.quit)
    
    def abrir_archivo(self):
        archivo=filedialog.askdirectory()
        if archivo:
            self.cargar_Imagenes(archivo)
            if self.lista_imagenes:
                self.mostrar_Imagenes(0)
            else:
                self.label_imagen.config(text="No se econtro imagenes en la carpeta seleccionada")

    def cargar_Imagenes(self,archivo):
        formatos_imagenes=('.png','.jpg','.jpeg','.gif','.webp')
        self.lista_imagenes=[os.path.join(archivo, file) for file in os.listdir(archivo) if file.lower().endswith(formatos_imagenes)]
        self.imagen_id_abrir=0


    def mostrar_Imagenes(self,id):
        if self.lista_imagenes:
            imagen_abrir=self.lista_imagenes[id]
            imagen=Image.open(imagen_abrir)
            imagen=imagen.resize((600,400))
            self.abrir_imagen=ImageTk.PhotoImage(imagen)

            self.label_imagen.config(image=self.abrir_imagen, text="")
        else:
            self.label_imagen.config(text="No hay imagenes para mostrar")
        
    def imagenAnterior(self):
        if self.lista_imagenes:
            self.imagen_id_abrir=(self.imagen_id_abrir-1)% len(self.lista_imagenes)
            self.mostrar_Imagenes(self.imagen_id_abrir)
    
    def imagenSiguiente(self):
        if self.lista_imagenes:
            self.imagen_id_abrir=(self.imagen_id_abrir+1)% len(self.lista_imagenes)
            self.mostrar_Imagenes(self.imagen_id_abrir)


ventana=tk.Tk()
app=Galeria(ventana)
ventana.mainloop()