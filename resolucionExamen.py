#Paso 1. Importamos las librerias
import sqlite3 as sq
from tkinter import *
from tkinter import messagebox

#Paso 2. Establecer una conexion a la base de datos
conexion=sq.connect('tienda.db')
cursor=conexion.cursor()

#Paso 3. Crear la tabla Categorias
cursor.execute('''CREATE TABLE IF NOT EXISTS Categorias(id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,nombre_categoria TEXT UNIQUE NOT NULL)''')

#Paso 4. Crear la tabla Productos
cursor.execute('''CREATE TABLE IF NOT EXISTS Productos(id_producto INTEGER PRIMARY KEY AUTOINCREMENT, nombre_producto TEXT NOT NULL, Precio REAL NOT NULL, Stock INTEGER NOT NULL, id_categoria INTEGER, FOREIGN KEY (id_categoria) REFERENCES Categorias(id_categorias)) ''')

#Paso 5. Crear la funcion para insertar una categoria
def insertarCategoria():
    nombre_categoria=entradaCategoria.get()
    if nombre_categoria:
        try:
            cursor.execute("INSERT INTO Categorias (nombre_categoria)VALUES(?)",(nombre_categoria,))
            conexion.commit()
            messagebox.showinfo("Registro exitoso","Categoria insertada correctamente")
        except sq.IntegrityError:
            messagebox.showerror("Error","La categoria ya existe ingrese uno nuevo")
    
    else:
        messagebox.showerror("Error","El campo categorias no puede estar vacio")

#Paso 6. Crear la funcion para insertar un producto
def insertarProducto():
    nombre_producto=entradaNombre.get()
    precio=entradaPrecio.get()
    stock=entradaStock.get()
    categoria=entradaIdCategoria.get()

    if nombre_producto and precio and stock and categoria:
        try:
            cursor.execute("SELECT id_categoria FROM Categorias WHERE id_categoria=?",(categoria,))
            resultado=cursor.fetchone()
            if resultado:
                cursor.execute("INSERT INTO Productos (nombre_producto,Precio,Stock,id_categoria)VALUES(?,?,?,?)",(nombre_producto,float(precio),int(stock),int(categoria)))
                conexion.commit()
                messagebox.showinfo("Registro Existoso","Producto insertado correctamente")
            else:
                messagebox.showerror("Error","La categoria no existe")
        except ValueError:
            messagebox.showerror("Error","Los datos de precio y stock deben ser numerico")
    else:
        messagebox.showerror("Error","Todos los campos deberan estar completos para insertar un productos")
#Paso 7. Creacion de la interfaz grafica
ventana=Tk()
ventana.title("Sistema de tienda en línea")
#Titulo y entrada de datos para la categoria
tituloCategoria=Label(ventana,text="Nombre de la Categorias: ")
tituloCategoria.grid(row=0,column=0, padx=10,pady=10)
entradaCategoria=Entry(ventana)
entradaCategoria.grid(row=0,column=1, padx=10, pady=10)
#Creacion del boton para insertar una categoria
botonInsertarCategoria=Button(ventana,text="Insertar Categoria",command=insertarCategoria)
botonInsertarCategoria.grid(row=0,column=2, padx=10,pady=10)

#Interfaz para productos
tituloNombreProducto=Label(ventana,text="Nombre del Producto: ")
tituloNombreProducto.grid(row=1,column=0, padx=10, pady=10)
entradaNombre=Entry(ventana)
entradaNombre.grid(row=1,column=1,padx=10,pady=10)

tituloPrecio=Label(ventana,text="Precio: ")
tituloPrecio.grid(row=2,column=0,padx=10,pady=10)
entradaPrecio=Entry(ventana)
entradaPrecio.grid(row=2,column=1,padx=10,pady=10)

tituloStock=Label(ventana,text="Stock: ")
tituloStock.grid(row=3,column=0,padx=10,pady=10)
entradaStock=Entry(ventana)
entradaStock.grid(row=3,column=1,padx=10,pady=10)

tituloIDCategoria=Label(ventana,text="ID categoria: ")
tituloIDCategoria.grid(row=4,column=0,padx=10,pady=10)
entradaIdCategoria=Entry(ventana)
entradaIdCategoria.grid(row=4,column=1,padx=10,pady=10)

#Boton para insertar un producto
botonInsertarProducto=Button(ventana,text="Insertar Producto", command=insertarProducto)
botonInsertarProducto.grid(row=5,column=0, columnspan=2, padx=10,pady=10)




ventana.mainloop()

#cerrar la conexion con la base 
conexion.close()

