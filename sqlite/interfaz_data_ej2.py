#Paso 1 importacion de sqlite3
import sqlite3
#Paso 2 Conectares a la base  de datos
coneion=sqlite3.connect('instituto.db')
#Paso 3. Crear cursores
datos=coneion.cursor()
#Paso 4. Crear una tabla
datos.execute('CREATE TABLE estudiante(ci INTEGER PRIMARY KEY,nombre TEXT NOT NULL,edad INTEGER,carrera TEXT NOT NULL)')
#Paso 5. Guadar los cambios
coneion.commit()
#Paso 6. Cerrar la conexion
coneion.close()






