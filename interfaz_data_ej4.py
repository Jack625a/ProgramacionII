#Paso 1. Importar las liberias
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

#Paso 2. Crear la venta principal
ventana=tk.Tk()
ventana.title("Base de Datos")

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

#Funcion para actualizar datos
def actualizarDatos():
    item=contenedor.selection()
    if not item:
        messagebox.showwarning("Adevertencia", "Seleccione un estudiante para actualizar. ")
        return
    registro=contenedor.item(item,'values')

    #Crear la nueva ventan para actualizar
    ventana_editar=tk.Toplevel()
    ventana_editar.title("Actualizacion de Datos")

    tk.Label(ventana_editar, text="Ci: ").grid(row=0,column=0)
    tk.Label(ventana_editar,text="Nombre: ").grid(row=1,column=0)
    tk.Label(ventana_editar,text="Edad: ").grid(row=2,column=0)
    tk.Label(ventana_editar, text="Carrera: ").grid(row=3, column=0)

    ci_actualizar=tk.StringVar(value=registro[0])
    nombre_actualizar=tk.StringVar(value=registro[1])
    edad_actualizar=tk.StringVar(value=registro[2])
    carrera_actualizar=tk.StringVar(value=registro[3])

    tk.Entry(ventana_editar,textvariable=ci_actualizar, state="readonly").grid(row=0,column=1)
    tk.Entry(ventana_editar,textvariable=nombre_actualizar).grid(row=1,column=1)
    tk.Entry(ventana_editar,textvariable=edad_actualizar).grid(row=2,column=1)
    tk.Entry(ventana_editar, textvariable=carrera_actualizar).grid(row=3,column=1)

    def guardarEstudiante():
        try:
            datos.execute(""" UPDATE estudiante SET nombre=?, edad=?, carrera=? WHERE ci=? """,(nombre_actualizar.get(),edad_actualizar.get(),carrera_actualizar.get(),ci_actualizar.get()))
            conexion.commit()

            messagebox.showinfo("Actualizacion","Estudiante actualizado correctamente.")
            cargarDatos()
            ventana_editar.destroy()
        except sqlite3.Error as e:
            messagebox.showerror("Error",f"No se pudo actual al estudiante: {e}")

    tk.Button(ventana_editar,text="Actualizar",command=guardarEstudiante).grid(row=4,column=0, columnspan=2)

    
#Funcion para eliminar a un estudiante
def eliminarEstudiante():
    item=contenedor.selection()
    if not item:
        messagebox.showwarning("Adevertencia","Seleccione un estudiante para eliminar")
        return
    registro=contenedor.item(item,'values')
    respuesta=messagebox.askyesno("Eliminacion",f"¿Esta seguro que desea eliminar al estudiante {registro[1]}?")
    if respuesta:
        try:
            datos.execute("DELETE FROM estudiante WHERE ci=?",(registro[0],))
            conexion.commit()
            messagebox.showinfo("Eliminacion","Estudiante eliminado correctamente.")
            cargarDatos()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"No se pudo eliminar al estudiante: {e}")

#Funcion para mostrar los detalles del estudiante seleccionado
def mostrarEstudiante(evento):
    item=contenedor.selection() #Obtiene el item seleccionado 
    if item:
        registro=contenedor.item(item,'values') #Obetiene los valores del item seleccionado
        mensanje=f"Ci:{registro[0]}\nNombre: {registro[1]} \nEdad: {registro[2]} \nCarrera: {registro[3]} "

        messagebox.showinfo("Detalles Estudiante",mensanje)

#Funcion para filtrar Carrera
def filtrarPorCarrera():
    carrera_seleccionada=selectorCarrera.get()
    cargarDatosFiltro(filtro_carrera=carrera_seleccionada)

#Funcion para realizar el filtrado de datos por la carrera
def cargarDatosFiltro(filtro_carrera=None):
    #recorremos a todos el contenedor y eliminamos todos los datos
    for fila in contenedor.get_children():
        contenedor.delete(fila)
    try:
        if filtro_carrera:
            datos.execute("SELECT * FROM estudiante WHERE carrera=?",(filtro_carrera,))
        else:
            datos.execute("SELECT * FROM estudiante")

        filas=datos.fetchall()
        for fila in filas:
            contenedor.insert("",tk.END,values=fila)
    except sqlite3.Error as e:
        messagebox.showerror("Error",f"Error al cargar los datos: {e}")
    




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
#Filtrado de datos
carreras=['Sistemas Informaticos','Diseño Grafico', 'Secretariado','Contaduria']
#Crearcion del comboBox
tk.Label(ventana,text="Filtrar por Carrera: ").grid(row=1,column=0)
selectorCarrera=ttk.Combobox(ventana,values=carreras)
selectorCarrera.grid(row=1,column=1)
botonFiltrar=tk.Button(ventana, text="Filtrar",command=filtrarPorCarrera)
botonFiltrar.grid(row=1,column=2)

#Botones para actualizar y eliminar a los estudiantes

botonActualizar=tk.Button(ventana, text="Actualizar Estudiante", command=actualizarDatos)
botonActualizar.grid(row=2, column=0)

botonEliminar=tk.Button(ventana,text="Eliminar Estudiante",command=eliminarEstudiante)
botonEliminar.grid(row=2,column=1)

#Paso 7. Cargar y mostrar los datos al iniciar la aplicacion
cargarDatos()

ventana.mainloop()

#Paso 8. Cerrar la conexion a la base de datos 
conexion.close()