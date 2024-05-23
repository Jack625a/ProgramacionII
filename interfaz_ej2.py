#Crear fguras en el lienzo con botones de movimiento
import tkinter as tk

#Crear las funciones de movimiento
def mover_izquierda():
    canvas.move(circulo,-10,0)
    canvas.move(rectangulo,-10,0)

def mover_derecha():
    canvas.move(circulo,10,0)
    canvas.move(rectangulo,10,0)

def mover_arriba():
    canvas.move(circulo,0,-10)
    canvas.move(rectangulo,0,-10)

def mover_abajo():
    canvas.move(circulo,0,10)
    canvas.move(rectangulo,0,10)

ventana=tk.Tk()
ventana.title("Lienzo con figuras en movimiento")


#Crear el Lienzo
canvas=tk.Canvas(ventana, width=400, height=400, bg="white")
canvas.pack()


#Dibujar el circulo y el rectangulo
circulo=canvas.create_oval(50,50,150,150, fill="blue")
rectangulo=canvas.create_rectangle(200,200,300,300, fill="red")

#crear los botones para mover las figuras
frame_Botones=tk.Frame(ventana)
frame_Botones.pack()

#Botones al frame
btnIzquierda=tk.Button(frame_Botones,text="Izquierda",command=mover_izquierda)
btnIzquierda.grid(row=0,column=0, padx=10)

btnDerecha=tk.Button(frame_Botones,text="Derecha",command=mover_derecha)
btnDerecha.grid(row=0,column=1,padx=10)

btnArriba=tk.Button(frame_Botones,text="Arriba",command=mover_arriba)
btnArriba.grid(row=0,column=2,padx=10)

btnAbajo=tk.Button(frame_Botones,text='Abajo',command=mover_abajo)
btnAbajo.grid(row=0,column=3,padx=10)



ventana.mainloop()