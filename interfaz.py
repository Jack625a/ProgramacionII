#Ventanas
#Paso 1 
import tkinter as tk #Importacion de los modulos de la interfaz grafica Tkinter

#Paso 2
#Crear una ventana
ventana=tk.Tk()
ventana.title("Ventana Interfaz")
ventana.geometry("300x500")


#Label
titulo=tk.Label(ventana,text="Programacion II")
titulo.grid(row=0,column=0)
titulo2=tk.Label(ventana,text="Texto 2")
titulo2.grid(row=1,column=1)

titulo3=tk.Label(ventana,text="texto3")
titulo3.grid(row=2,column=2)


#Posicionamineto de componentes
#PACK: HORIZONTAL O VERTICAL ()
#GRID: COLUMNAS Y FILAS (ROW,COLUMN)
#PLACE: POSICIONES ABSOLUTAS (COORDENADAS X,Y)






#Paso 3
#Mostrar la ventana
ventana.mainloop()