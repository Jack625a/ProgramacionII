#Herencia: Permite crear nuevas clases basadas en otra clase 
         #Clase Padre (SUPERCLASE)
#Clase hijo(SUBCLASES)     Clase hijo (SUBCLASES)

#Ej.1-11/04/2024 - Crear una superclase Animal con sus subclases
class Animal:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    #Crear las acciones de la clase
    def sonido(self):
        print("Sonido que realiza el animal")
    def comer(self):
        print(self.nombre+" Esta Comiendo ...")

#Subclases
class Perro(Animal):
    def caminar(self):
        print(self.nombre+" esta corriendo")

class Gato(Animal):
    def dormir(self):
        print(self.nombre +" esta durmiendo")

#Crear los objetos de la superclase 
perro=Perro("Scott",4)
perro.comer()
perro.caminar()

gato=Gato("Tom",2)
gato.comer()
gato.dormir()


