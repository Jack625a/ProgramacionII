#Ventanas Secundarias
#TopLevel: Permite crear ventas secundarias
import tkinter as tk
#Cjas de dialogo
from tkinter import filedialog
#Color de las cajas de dialogo
from tkinter import colorchooser

def crearNuevaVenta():
    nuevaVentana=tk.Toplevel(ventana)
    tk.Label(nuevaVentana, text='Ventana Secundaria').pack()

def abrirArchivo():
    abrir=filedialog.askopenfilename()
    if abrir:
        print(f"Archivo seleccionado: {abrir}")

def cambiarColorDialogo():
    color=colorchooser.askcolor(title="Cambio de Color")
    if color:
        print(f"Color seleccionado: {color}")


ventana=tk.Tk()
tk.Button(ventana, text='Abrir Nueva Ventana', command=crearNuevaVenta).pack()
tk.Button(ventana,text='Abrir Archivos',command=abrirArchivo).pack()
tk.Button(ventana, text='Cambiar Color',command=cambiarColorDialogo).pack()

ventana.mainloop()

