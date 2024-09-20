#Clase padre (MaterialBiblioteca)
#Atributos de la clase padre(titulo,autor,año_publicacion,tipo)
#Subclases (Libro,Revista,Periodico)
#METODO O ACCION
#tomar_presatado
#devolver
#Clase padre (UsuarioBiblioteca)
#Atributos de la clase padre (nombre,edadd,tipo_documento,numero_documento)
#Subclases (Estudiante,Profesor,Visitante)

class MaterialBiblioteca:
    def __init__(self,titulo,autor,año_publicacion,tipo):
        self.titulo=titulo


    #Metodos o acciones
    def tomar_prestado(self): #Polimorfismo
    
    def devolver(self):#Polimorfismo

    def mostrarMateriales(self):

    def añadirMaterial(self):


#Subclases de la clase padre MaterialBiblioteca
class Libro(MaterialBiblioteca):
    def __init__(self,titulo,autor,año_publicacion,tipo,editorial,edicion,isbn):
        super().__init__(titulo,autor,año_publicacion,tipo)
        self.editorial=editorial
        self.edicion=edicion
        self.isbn=isbn

    #def añadirLibro(self,libro):


class Revista(MaterialBiblioteca):

class Periodico(MaterialBiblioteca):



class UsuarioBiblioteca:
    def __init__(self,nombre,edad,tipo_Documento,numero_documento):

    #metodos o acciones

    def tomar_prestado():

    def devolver():
    
    def mostrarUsuarios():

    def agregarUsuarios()
        

class Estudiante(UsuarioBiblioteca):
    def __init__(self,nombre,edad,tipo_Documento,numero_documento,carrera):
        super().__init__(nombre,edad,tipo_Documento,numero_documento)
        self.carrera=carrera

    def tomar_prestado():

    def devolver():

class Profesor(UsuarioBiblioteca):
    def __init__(self,nombre,edad,tipo_Documento,numero_documento,profesion):
        super().__init__(nombre,edad,tipo_Documento,numero_documento)
        self.profesion=profesion
    def tomar_prestado():

    def devolver():

class Visitante(UsuarioBiblioteca):
    def __init__(self,nombre,edad,tipo_Documento,numero_documento,contraseña):
        super().__init__(nombre,edad,tipo_Documento,numero_documento)
        self.contraseña=contraseña

    def tomar_prestado():

    def devolver():




libro1=Libro()
revista1=Revista()
periodico1=Periodico()
estudiate1=Estudiante()
profesor1=Profesor()
visitante1=Visitante()

libros=[]
revistas=[]
periodicos=[]


print("Sistema Gestion Biblioteca")
print("1. Agregar Usuarios")
print("2. Agregar Material")
print("3. Mostrar Usuarios")
print("4. Mostrar Materiales")

print("5. Prestar Material")
print("6. Devolver Material")


