#Estructura basica de la Programacion Orientada a Obejtos
#PASO 1. CREAR LA CLASE
class Auto:
    #Definimos el constructor
    def __init__(self,color, marca, modelo, combustible):
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.combustible=combustible
        self.velocidad=0
        self.nivelCombustible=0
    
    #PASO 2. CREAR LAS ACCIONES O METODOS DE LA CLASE
    def acelerar(self,incremento):
        self.velocidad+=incremento
        print(f"El auto {self.marca} esta acelarando a una velocidad de {self.velocidad} Km/h")
    
    def frenar(self,decremento):
        if self.velocidad>=decremento:
            self.velocidad-=decremento
            print(f"El auto {self.marca} desacelero {decremento} km/h, la velocidad actual es {self.velocidad}")
        else:
            self.velocidad=0

    def tocarBocina(self):
        print(f"El auto {self.marca} esta tocando la Bocina")

    def llenarCombustible(self,carga):
        
        self.nivelCombustible+=int(carga)
        
        if self.nivelCombustible==0:
            print(f"El nivel de combustible del auto {self.marca} esta vacio realice la carga de combustible!")
            cargado=int(input("Ingrese la cantidad de carga: "))
            self.nivelCombustible+=cargado
            print(f"El nivel de carga del auto {self.marca} es de {self.nivelCombustible}%")
        elif self.nivelCombustible<=20:
            print(f"Nivel de carga bajo ({carga}) del auto {self.marca}")
            alerta=input("Desea realizar la carga de combustible? 1.Si, 2.No: ")
            if alerta=="Si":
                carga=int(input("Ingrese la cantidad de carga: "))
                self.nivelCombustible+=carga
                print(f"El nivel de carga del auto {self.marca} es de {self.nivelCombustible}%")
        else:
            self.nivelCombustible=0


#PASO 3. DEFINIR LOS OBJETOS DE LA CLASE
auto1=Auto("Rojo","Toyota","Prius","Gasolina")
auto2=Auto("Azul","Audi","A4","Diesel")
auto3=Auto("Negro","Kia","Z10","Electrico")
auto4=Auto("Blanco","Nissan","Sedan","Gasolina")

auto1.tocarBocina()
auto3.tocarBocina()
auto4.tocarBocina()



auto2.acelerar(50)
auto1.acelerar(100)
auto3.acelerar(100)
auto4.acelerar(80)

auto1.frenar(20)
auto4.frenar(50)

print("----------------")
auto1.llenarCombustible(0)
print("----------------")
auto3.llenarCombustible(15)
print("----------------")
auto4.llenarCombustible(100)
print("-----------------")
auto2.llenarCombustible(19)