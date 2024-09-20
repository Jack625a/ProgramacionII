#Crear una clase para emular un Banco
#Clase Banco
#Acciones => Retirar Dinero, Depositar Dinero, Obtener Extracto, Crear Cuenta.
#Parametros => 




#PASO 1.  CREAR CLASE
class Banco:
    #Definir el constructor
    def __init__(self,nombreBanco):
        self.nombreBanco=nombreBanco
        self.usuarios={}
    
    #PASO 2. Crear las acciones de la clase
    def crearCuenta(self,nombre,ci,correo,celular):
        print("---Creacion de Cuenta Bancaria---")
        cuenta=CuentaBancaria(nombre,ci,correo,celular)
        self.usuarios[ci]=cuenta
        print("El Registro del usuario ",cuenta.nombre, " se realizo correctamente...")
    
    def depositar(self, ci,monto):
        #Verificar que la cuenta existe
        if ci in self.usuarios:
            self.usuarios[ci].saldo += monto
            print("Se realizo el deposito de ",monto, "Bs en la cuenta de ",self.usuarios[ci].nombre, " Saldo total: ",self.usuarios[ci].saldo,"Bs")
        else:
            print("Error usuario no encontrado...")


    def retirar(self,ci,monto):
        #Verificar que la cuenta existe
        if ci in self.usuarios:
            if self.usuarios[ci].saldo>=monto:
                self.usuarios[ci].saldo -= monto
                print("Se retiro el monto de ",monto, "Bs de la cuenta de ",self.usuarios[ci].nombre, " Saldo total: ",self.usuarios[ci].saldo,"Bs")
            else:
                print("Error saldo insuficiente")
    
    def obtenerExtracto(self,ci):
        #Verificar que la cuenta existe
        if ci in self.usuarios:
            print("---Extracto Bancario----")
            print("Nombre: ",self.usuarios[ci].nombre)
            print("CI: ",ci)
            print("Saldo: ", self.usuarios[ci].saldo,"Bs")
        else:
            print("Usuario no encontrado...")

#Segunda Alternativa podemos crear una clase para creacion de cuenta
class CuentaBancaria:
    def __init__(self,nombre,ci,correo,celular):
        self.nombre=nombre
        self.ci=ci
        self.correo=correo
        self.celular=celular
        self.saldo=0



#Paso 3.  Crear los objetos de la clase

#banco.crearCuenta("Kevin Arroyo", 7455512,"a@gmail.com",74555132)
#banco.depositar(7455512,1000)
#banco.retirar(7455512,555)
#banco.obtenerExtracto(7455512)


##Mejoras
#Crear un menu para las acciones en el Banco

def menu():
    print("---Bienvenid@ al Banco")
    print("1. Crear Cuenta")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Obtener Extracto")
    print("0. Salir")
    return input("Seleccione una opcion: ")

banco=Banco("Banco Union")
while True:
    selecion=menu()
    if selecion=="1":
        nombre=input("Ingrese su nombre completo: ")
        ci=int(input("Ingrese su carnet de identidad: "))
        correo=input("Ingrese su correo: ")
        celular=int(input("Ingrese su celular: "))
        banco.crearCuenta(nombre,ci,correo,celular)
    elif selecion=="2":
        ci=int(input("Ingrese su carnet de identidad: "))
        monto=int(input("Ingrese el monto a depositar: "))
        banco.depositar(ci,monto)
    elif selecion=="3":
        ci=int(input("Ingrese su carnet de identidad: "))
        monto=int(input("Ingrese el monto a depositar: "))
        banco.retirar(ci,monto)
    elif selecion=="4":
        ci=int(input("Ingrese su carnet de identidad: "))
        banco.obtenerExtracto(ci)
    elif selecion=="0":
        print("Gracias... ",banco.nombreBanco)
        break
    else:
        print("Opcion no valida....")


