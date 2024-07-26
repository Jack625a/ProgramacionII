#Datos locales - Cargar, Guardar, Manipular los datos locales 
#Paso 1. Importar los modulos
import tkinter as tk
from tkinter import messagebox, filedialog
import os

#Paso 2. Crear la clase App
class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestión de datos locales")
        #Paso 3. Crear los componentes de la interfaz
        self.titulo=tk.Label(ventana, text="Ingrese los datos: ")
        self.titulo.pack(pady=5)

        self.texto=tk.Text(ventana, height=10, width=50)
        self.texto.pack(pady=5)

        self.guardarBoton=tk.Button(ventana, text="Guardar Datos", command=self.guardar_datos)
        self.guardarBoton.pack(padx=10,pady=5, side=tk.LEFT)

        self.cargarBoton=tk.Button(ventana,text="Cargar Datos", command=self.cargar_datos)
        self.cargarBoton.pack(side=tk.LEFT, padx=10, pady=5)

        self.eliminarBoton=tk.Button(ventana,text="Eliminar Datos", command=self.eliminar_datos)
        self.eliminarBoton.pack(side=tk.LEFT,padx=10,pady=5)

    
    #Paso 4. Creacion de las acciones o metodos de la clase
    def guardar_datos(self):
        datos=self.texto.get("1.0",tk.END)
        archivo=filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Texto","*.txt"),("Todos","*.*")])
        if archivo:
            with open(archivo,'w') as file:
                file.write(datos)
            messagebox.showinfo("Exito","Datos guardados correctamente")

    def cargar_datos(self):
        archivo=filedialog.askopenfilename(filetypes=[("Texto","*.txt"),("Todos","*.*")])
        if archivo:
            with open(archivo,'r') as file:
                datos=file.read()
                self.texto.delete("1.0",tk.END)
                self.texto.insert(tk.END,datos)
            messagebox.showinfo("Exito","Datos cargados correctamente")
    def eliminar_datos(self):
        archivo=filedialog.askopenfilename(filetypes=[("Texto","*.txt*"),("Todos","*.*")])
        if archivo:
            confirmacion=messagebox.askyesno("Confirmar",f"¿Seguro que desea eliminar {os.path.basename(archivo)}??")
            if confirmacion:
                os.remove(archivo)
                messagebox.showinfo("Exito","Archivo eliminado correctamente")

ventana=tk.Tk()
Aplicacion=App(ventana)
ventana.mainloop()