#Tabla: Categorías - Productos

#Paso 1. Importacion de las librerias
import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter as tk

#Paso 2. Establecer una conexion con la base de datos
conexion=sqlite3.connect('tienda.db')
