#EJe1. Integrar los componentes de lable boton y radiobutton para mostrar al usuario varias frutas para que pueda eligir uno


#LABEL, RADIOBUTTONS, BUTTON
import tkinter as tk
from tkinter import messagebox

#Funcion para mostrar la fruta que seleccione el usuario
def mostrar():
    seleccionFruta=f"Fruta seleccionada: {frutaSeleccionada.get()}"
    seleccion.config(text=seleccionFruta)
    messagebox.showinfo("Fruta seleccionada", seleccionFruta)




ventana=tk.Tk()
ventana.title("Frutas")
#Label Titulo
titulo=tk.Label(ventana,text="Seleccione su fruta favorita!")
titulo.pack(pady=10,padx=10)

#RadioButtton opciones de frutas
#fruta1=tk.Radiobutton(ventana,text="Manzana")
frutaSeleccionada=tk.StringVar(value="Manzana")
frutas=["Manzana","Naranja","Pera","Sandia","Banana","Uva","Frutilla"]
for fruta in frutas:
    opciones=tk.Radiobutton(ventana,text=fruta,variable=frutaSeleccionada,value=fruta)
    opciones.pack()

#Boton 
boton=tk.Button(ventana,text="Enviar", command=mostrar)
boton.pack(pady=10)

#Label Mostrar la seleccion de la fruta 
seleccion=tk.Label(ventana,text="")
seleccion.pack(pady=20)




ventana.mainloop()