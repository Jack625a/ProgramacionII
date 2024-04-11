#POLIMORFISMO: PERMITE QUE LOS OBJETOS DE DIFERENTES CLASES PUEDAN HEREDAR Y MODIFICAR LAS ACCIONES O METODOS


#Ej.1-11/04/2024 - Crear una superclase Animal con sus subclases , aplicar el polimorfismo
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
    def comer(self):
        print("El perro de nombre "+self.nombre+" Esta Comiendo ...")

class Gato(Animal):
    def dormir(self):
        print(self.nombre +" esta durmiendo")
    def comer(self):
        print("El gato de nombre "+self.nombre+" Esta Comiendo ...")


perro=Perro("Scott",2)
gato=Gato("Tom",4)

perro.comer()
gato.comer()


