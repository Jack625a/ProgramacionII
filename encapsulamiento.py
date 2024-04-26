#Encapsulamiento: Refiere a la forma de permitir el accesos a los atributos y metodos pero solamente a traves de una interfaz publica
#Puntos clave del encapsulamiento Python
#1. Convecciones de Nomenclatura
    #_ (1 guion bajo ->Datos Protegidos) Atributos Protegidos
    #__ (2 guiones bajo -> Datos privadops) Atributo o Metodos (Privados)
#2. Metodos de Acceso
    #GETTERS Y SETTERS (LEER O MODIFICAR LOS ATRIBUTOS PRIVADOS,PROTEGIDOS)
#3. Uso de Propiedades
    #Permiten definir comportamientos personalizados

#PROGRAMACION ORIENTADA A OBJETOS

class Estudiantes:
    def __init__(self,nombre,edad,carrera,celular,contraseña,correo):
        self._nombre=nombre #atributo protegido
        self.edad=edad #atributo publico
        self.celular=celular
        self.carrera=carrera
        self.__contraseña=contraseña#Atributos Privados
        self.__correo=correo#Atributos Privado

    #METODOS DE ACCESO PARA OBTENER EL NOMBRE
    def get_nombre(self):
        return self._nombre
    
    #METODO DE ACCESO PARA ESTABLECER UN NUEVO NOMBRE
    def set_nombre(self,nombre):
        self._nombre=nombre

    #METODOS DE ACCESO PARA OBTENER LA CONTRASEÑA Y EL CORREO
    def get_contraseña(self):
        return self.__contraseña
    
    def get_correo(self):
        return self.__correo
    
    #METODOS DE ACCESO PARA ESTABLECER CONTRASEÑA Y CORREO

    def set_contraseña(self,contraseña):
        self.__contraseña=contraseña
    
    def set_correo(self,correo):
        self.__correo=correo

#Creacion de los objetos de la clase
estudiante1=Estudiantes("Kevin Arroyo",28,"Sistemas Informaticos",75426265,"123456789","k@gmail.com")

print("Acceder a los atributos a traves de sus metodos de acceso")
##Acceder a los atributos a traves de sus metodos de acceso
print(estudiante1.get_correo())
print(estudiante1.get_contraseña())
print(estudiante1.get_nombre())


print("Modificar atributos a traves de los metodos de acceso")
nuevonombre="Juan Perez"
#Modificar atributos a traves de los metodos de acceso
estudiante1.set_nombre(nuevonombre)
estudiante1.set_contraseña("abcd123+123")

#Verficacion de los cambios
print(estudiante1.get_nombre())
print(estudiante1.get_contraseña())