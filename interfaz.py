#Ventanas
#Paso 1 

#Funcion para el boton 1 - Escribir en la terminal
def prueba():
    print("Mensaje de prueba del boton...")
    titulo3.config(text="texto3")

#Funcion para el boton 2 - modificar texto de un label
def modificar():
    nombreLabel=nombre.get()
    descripcionNuevo=mensaje.get("1.0",tk.END).strip() #Elimina los espacios en blanco al final del multilinea
    titulo2.config(text=descripcionNuevo)
    titulo3.config(text=nombreLabel)



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

#Botones
boton1=tk.Button(ventana, text="Boton 1", command=prueba)
boton1.grid(row=3,column=1)

boton2=tk.Button(ventana,text="Boton 2", command=modificar)
boton2.grid(row=4,column=1)

#ENTRADA DE DATOS (Entry): Campo de texto para entrada de datos
nombre=tk.Entry(ventana)
nombre.grid(row=5,column=1)

#CAMPOS DE TEXTO MULTILINEA (Text)
mensaje=tk.Text(ventana,height=8,width=30)
mensaje.grid(row=6,column=1)


#Casillas de Verificacion (Marcar o desmarcar) CheckButton
op1=tk.Checkbutton(ventana, text="Opcion 1")
op1.grid(row=7,column=1)

op2=tk.Checkbutton(ventana,text="Opcion 2")
op2.grid(row=8,column=1)

#Botones de Opciones (Seleccionar una opcion) RadioButton
respuesta=tk.StringVar(value="opcion1")
opc1=tk.Radiobutton(ventana, text="Opcion 1",value="opcion1",variable=respuesta)
opc2=tk.Radiobutton(ventana, text="Opcion 2", value="opcion2", variable=respuesta)
opc3=tk.Radiobutton(ventana, text="Opcion 3",value="opcion3",variable=respuesta)
opc4=tk.Radiobutton(ventana, text="Opcion 4", value="opcion4", variable=respuesta)
opc1.grid(row=9,column=1)
opc2.grid(row=10,column=1)
opc3.grid(row=11,column=1)
opc4.grid(row=12,column=1)


#Paso 3
#Mostrar la ventana
ventana.mainloop()
