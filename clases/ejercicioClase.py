#Una pantalla con 4 entradas de datos y un boton
import tkinter as tk


def mostrar():
    print("")
    


ventana=tk.Tk()

ventana.title("Ejercicio Clase")
entrada1=tk.Entry(ventana)
entrada1.pack()
entrada2=tk.Entry(ventana)
entrada2.pack()
entrada3=tk.Entry(ventana)
entrada3.pack()
entrada4=tk.Entry(ventana)
entrada4.pack()

boton=tk.Button(ventana, text="Mostrar")
boton.pack()


ventana.mainloop()