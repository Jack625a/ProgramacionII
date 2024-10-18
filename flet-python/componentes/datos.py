import sqlite3

# Crear la base de datos y la tabla si no existen
def create_database():
    conn = sqlite3.connect("tienda.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            precio REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Insertar algunos productos de ejemplo
def insert_data():
    conn = sqlite3.connect("tienda.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, descripcion, precio) VALUES ('Producto 1', 'Descripcion del producto 1', 19.99)")
    cursor.execute("INSERT INTO productos (nombre, descripcion, precio) VALUES ('Producto 2', 'Descripcion del producto 2', 29.99)")
    cursor.execute("INSERT INTO productos (nombre, descripcion, precio) VALUES ('Producto 3', 'Descripcion del producto 3', 39.99)")
    conn.commit()
    conn.close()

create_database()  # Ejecutar solo una vez
# insert_data()  # Ejecutar si necesitas insertar los productos
