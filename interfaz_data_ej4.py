#Paso 1. Importar las liberias
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

#Paso 2. Crear la venta principal
ventana=tk.Tk()
ventana.title("Obtencion de datos")

#Paso 3. Establecer una conexion a la base de datos
conexion=sqlite3.connect('instituto.db')
#Paso 4. Configuracion del cursor
datos=conexion.cursor()

#Paso 5. Funcion para obtener y mostrar los datos 
def cargarDatos():
    #Eliminacion de todos los datos que tenga el contenedor
    for fila in contenedor.get_children():
        contenedor.delete(fila)

    #Seleccionamos todos los registros de la tabla Estudiante
    datos.execute("SELECT * FROM estudiante")
    filas=datos.fetchall()
    for fila in filas:
        contenedor.insert("",tk.END, values=fila)


#Funcion para mostrar los detalles del estudiante seleccionado
def mostrarEstudiante(evento):
    item=contenedor.selection() #Obtiene el item seleccionado 
    if item:
        registro=contenedor.item(item,'values') #Obetiene los valores del item seleccionado
        mensanje=f"Ci:{registro[0]}\nNombre: {registro[1]} \nEdad: {registro[2]} \nCarrera: {registro[3]} "

        messagebox.showinfo("Detalles Estudiante",mensanje)

#Paso 6. Creacion de la interfaz con el componente treeView para mostrar los datos de los estudiantes
columnas=("Ci", "Nombre","Edad", "Carrera")
contenedor=ttk.Treeview(ventana, columns=columnas, show="headings")

contenedor.heading("Nombre",text="Nombre")
contenedor.heading("Ci",text="Ci")
contenedor.heading("Edad",text="Edad")
contenedor.heading("Carrera",text="Carrera")
#Vincular el evento del click en el contenedor(TreeView) a la funcion de mostrarEstudiante
contenedor.bind("<ButtonRelease-1>",mostrarEstudiante)

contenedor.grid(row=5,column=0, columnspan=2)


#Paso 7. Cargar y mostrar los datos al iniciar la aplicacion
cargarDatos()


ventana.mainloop()

#Paso 8. Cerrar la conexion a la base de datos 
conexion.close()