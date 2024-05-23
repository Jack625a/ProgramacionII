#Componentes Avanzados para la interfaz grafica
#Canvas: Permite representar aspectos visuales
import tkinter as tk

ventana=tk.Tk()
ventana.title('Componentes Avanzados')

#Lienzos
canvas=tk.Canvas(ventana,width=400, height=400)
canvas.pack()

#Dibujar un rectangulo
canvas.create_rectangle(50,150,100,100, fill="red")
#Dibujar un ovalo
canvas.create_oval(200,50,300,150, fill="green")
#Dibujar Linea
canvas.create_line(0,0,400,300, fill="blue")
#Dibujar Texto
canvas.create_text(150,150,fill="Black",text='Hola')

ventana.mainloop()