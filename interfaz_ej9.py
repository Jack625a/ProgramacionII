#Variables de control Numericos - SPINBOX
import tkinter as tk
from tkinter import messagebox

#Creacion de la clase
class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Variables con control Numericos")

        #Definimos las variables de control
        self.valor=tk.IntVar(value=0)

        #Creacion del spinbox para el uso de cambio en la variable de control
        self.spinbox=tk.Spinbox(ventana,from_=0,to=20, textvariable=self.valor)
        self.spinbox.pack(pady=10)

        self.boton=tk.Button(ventana,text="Mostrar Valor", command=self.mostrar)
        self.boton.pack(pady=10)

    #Accion de la clase
    def mostrar(self):
        valor=self.valor.get()
        messagebox.showinfo("Valor seleccionado ",f"El valor seleccionado es: {valor}")


ventana=tk.Tk()
app=App(ventana)
ventana.mainloop()