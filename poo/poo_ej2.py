#Crear una clase para la materia de Programacion II 
#Estudiantes
#Docentes
#Paso 1. Crear la clase
class Estudiante:
    #Definimos el contructor
    def __init__(self,nombre,edad,celular,nota):
        self.nombre=nombre
        self.edad=edad
        self.celular=celular
        self.nota=nota
    
    #Paso 2. Definimos las acciones o metodos de la clase
    def mostrarInformacion(self):
        print("---Información del Estudiante---")
        print("Nombre: ",self.nombre, " Edad: ",self.edad," años")
        print("Celular: ",self.celular)
        print("Nota: ",self.nota)
    
    def estudiar(self):
        print(self.nombre, "esta estudiando...")
    
    

#Paso 3. Crear el obejto perteneciente a la clase Estudiante
estudiante1=Estudiante("Kevin Arroyo",27,65425546,80)
estudiante2=Estudiante("Juan",26,73845123,100)


estudiante1.mostrarInformacion()
estudiante2.mostrarInformacion()
estudiante1.estudiar()


 


