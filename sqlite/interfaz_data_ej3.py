#Paso 1. Importacion  de las librerias
import tkinter as tk
from tkinter import messagebox
import sqlite3

#Paso 2. Creacion de la ventana principal
ventana=tk.Tk()
ventana.title("Base de datos")

#Paso 3. Crear una conexion a la base de datos
conexion=sqlite3.connect('instituto.db')
#Paso 4. Crearcion del cursos
datos=conexion.cursor()
#Paso 5. Consulta sql para insercion de datos
def addEstudiante():
    nombre=nombre_entry.get()
    ci=ci_entry.get()
    carrera=carrera_entry.get()
    edad=edad_entry.get()

    if nombre and ci and carrera and edad:
        #Paso 6. Ejecutar la consulta sql
        conexion.execute("INSERT INTO estudiante(ci,nombre,edad,carrera) VALUES(?,?,?,?)",(ci,nombre,edad,carrera))
        #Paso 7. Guardar los cambios
        conexion.commit()
        messagebox.showinfo("Completado","Estudiante agregado correctamente!")
        ci_entry.delete(0, tk.END)
        nombre_entry.delete(0, tk.END)
        edad_entry.delete(0, tk.END)
        carrera_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error","Ingrese todos los datos para continuar")





#Interfaz grafica
tk.Label(ventana, text="Nombre: ").grid(row=0, column=0)
tk.Label(ventana,text="Carnet de Identidad: ").grid(row=1,column=0)
tk.Label(ventana,text="Carrera: ").grid(row=2, column=0)
tk.Label(ventana,text="Edad: ").grid(row=3,column=0)

nombre_entry=tk.Entry(ventana)
nombre_entry.grid(row=0, column=1)
ci_entry=tk.Entry(ventana)
ci_entry.grid(row=1, column=1)
carrera_entry=tk.Entry(ventana)
carrera_entry.grid(row=2,column=1)
edad_entry=tk.Entry(ventana)
edad_entry.grid(row=3,column=1)




#Boton para agregar un estudiante
boton=tk.Button(ventana,text="Añadir Estudiante", command=addEstudiante)
boton.grid(row=4, columnspan=2)


ventana.mainloop()


conexion.close()