#PanelWindows
#Permite dividir el area de la aplicacion
import tkinter as tk
from tkinter import ttk

ventana=tk.Tk()
ventana.title('Paneles')


panel=ttk.PanedWindow(ventana,orient=tk.HORIZONTAL)
panel.pack(fill=tk.BOTH, expand=True)


frame1=ttk.Frame(panel, width=200, height=200 )
frame2=ttk.Frame(panel,width=300, height=200)
panel.add(frame1,weight=1)
panel.add(frame2,weight=4)

titulo=tk.Label(frame1,text='Pantalla 1')
titulo.pack()
#Spinbox
#Componentes que permite seleccionar al usuario valores de una secuaencia

spinner=tk.Spinbox(frame1, from_=0, to=10)
spinner.pack()

titulo2=tk.Label(frame2,text='Pantalla 2')
titulo2.pack()
#Progressbar
#Componente para mostrar progreso de una operacion
progreso=ttk.Progressbar(frame2,orient=tk.HORIZONTAL,length=100,mode='determinate')
progreso.pack()


#Funcion para iniciar el progreso
def incioProgreso():
    progreso['value']=0
    frame2.update_idletasks()
    for i in range (101):
        progreso['value']=i
        frame2.update_idletasks()
        frame2.after(50)


#Boton para activar el Progressbar
boton=tk.Button(frame2, text='Iniciar', command=incioProgreso)
boton.pack()







ventana.mainloop()


