#Sistema de gestion de tienda de productos online
#Clase principal (PADRE) = PRODUCTOS

class Producto:
    productos_disponibles=[]
    def __init__(self,nombre,precio,descripcion):
        self.nombre=nombre
        self.precio=precio
        self.descripcion=descripcion
        Producto.productos_disponibles.append(self)
    #Acciones o metodos de la clase
    def calcularPrecioProducto(self,cantidad):
        return self.precio*cantidad
    
    def mostrarProductos():
        print("Productos Disponibles")
        for producto in Producto.productos_disponibles:
            print (f"{producto.nombre} - Precio: {producto.precio} - Descripcion: {producto.descripcion}")

#Herencia SUBCLASE
class Descuentos(Producto):
    def __init__(self,nombre,precio,descripcion,descuento):
        super().__init__(nombre,precio,descripcion) 
        self.descuento=descuento
    #Acciones o metodos de la subclase
    def calcularPrecioProducto(self,cantidad):
        precio_sin_descuento=super().calcularPrecioProducto(cantidad)  
        precio_con_descuento=(precio_sin_descuento*self.descuento)/100
        return precio_con_descuento

class Carrito:
    def __init__(self):
        self.productos=[]
    
    #ACCIONES DEL CARRITO
    def agregarProducto(self,producto,cantidad):
        self.productos.append({"producto":producto, "cantidad":cantidad})
    
    def total(self):
        total=0
        for producto in self.productos:
            total+=producto["producto"].calcularPrecioProducto(producto["cantidad"])
        return total
    
    def mostrarCarrito(self):
        if not self.productos:
            print("El carrito esta vacio...")
        else:
            print("MI CARRITO")
            for producto in self.productos:
                print(f"{producto['producto'].nombre} - Cantidad: {producto['cantidad']}")



##Crear los objetos de clase
producto1=Producto("Coca-Cola 300 Ml 6pack",18,"Botella No Retornable")
producto2=Producto("Vital Sin Gas 600 Ml 6pack",27,"Agua")
producto3=Producto("Del Valle Fresh Fruit Punch 300 Ml 6pack", 18,"Fruit Punch")
producto4=Producto("Monster Ultra 473 Ml 6pack",102,"Energizante")
producto5=Producto("Fanta Naranja 3 Lt 6pack",84,"Fanta")
#PRODUCTOS EN DESCUENTO
producto6=Descuentos("Del Valle Fresh Fruit Punch 300 Ml 6pack", 18,"Fruit Punch",20)
producto7=Descuentos("Monster Ultra 473 Ml 6pack",102,"Energizante",50)
producto8=Descuentos("Fanta Naranja 3 Lt 6pack",84,"Fanta",30)

#Mostrar los Productos Disponibles
Producto.mostrarProductos()

print("TIENDA COCA COLA")

accion=True
while(accion):
    print("1. Mostrar Productos")
    print("2. Agregar Productos")
    print("3. Ver Carrito")
    print("4. Salir")
    seleccion=input("Seleccione una opcion")
    
    if seleccion=="1":
        Producto.mostrarProductos()
    elif seleccion=="2":
        carrito=Carrito()
        producto=input("Agregue el producto: ")
        cantidad=int(input("Ingrese la cantidad: "))
        carrito.agregarProducto(producto,cantidad)
        carrito.mostrarCarrito()

        #print("TOTAL A PAGAR: ", carrito.total())
    elif seleccion=="3":
        print("TOTAL A PAGAR: ", carrito.total())
    elif seleccion=="4":
        print ("Gracias por su compra")
        accion=False
    else:
        accion=False

#CREAR EL CARRITO Y AGREGAGR PRODUCTOS

#carrito.agregarProducto(producto1,2)
#carrito.agregarProducto(producto6,5)
#carrito.agregarProducto(producto8,4)

#MOSTRAR EL CONTENIDO DEL CARRITO DE COMPRAS Y TOTAL A PAGAR
#carrito.mostrarCarrito()
#print("TOTAL A PAGAR: ", carrito.total())


