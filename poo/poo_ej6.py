#Ejercicio Completo -POO - HERENCIA - POLIMORFISMO 
#Crear un sistema para el instituto Khanamarka
#Docentes, Estudiantes, Administrativos
#SUPER CLASE
class PersonasInstituto:
    def __init__(self,nombre,edad,celular):
        self.nombre=nombre
        self.edad=edad
        self.celular=celular
    ##Acciones o Metodos
    def detalleRegistro(self):
        return f"Nombre: {self.nombre} - Edad: {self.edad} - Celular: {self.celular}" 

##SUBCLASES
class Docente(PersonasInstituto):
    def __init__(self,nombre,edad,celular, profesion, salario):
        super().__init__(nombre,edad,celular)
        self.profesion=profesion
        self.salario=salario
    
    def detalleRegistro(self):
        return f"**DOCENTE***  Nombre: {self.nombre} - Edad: {self.edad} - Celular: {self.celular} - Profesion: {self.profesion} - Salario: {self.salario}" 
    

##SUBCLASE ESTUDIANTES
class Estudiante(PersonasInstituto):
    def __init__(self,nombre,edad,celular,carrera):
        super().__init__(nombre,edad,celular)
        self.carrera=carrera
    def detalleRegistro(self):
        return f"**ESTUDIANTE***  Nombre: {self.nombre} - Edad: {self.edad} - Celular: {self.celular} - Carrera: {self.carrera}"


#Subclase Administrativos
class Administrativo(PersonasInstituto):
    def __init__(self, nombre, edad, celular,cargo,profesion):
        super().__init__(nombre, edad, celular)
        self.cargo=cargo
        self.profesion=profesion
    def detalleRegistro(self):
        return f"**ADMINISTRATIVO*** Nombre: {self.nombre} - Edad: {self.edad} - Celular: {self.celular} - Cargo: {self.cargo} - Profesion: {self.profesion}" 
    


docente1=Docente("Kevin Arroyo",27,75454852,"Ing. Sistemas",1000)
estudiante1=Estudiante("Juan",25,755451,"Sistemas Informaticos")
administrativo1=Administrativo("Jose",30,7554541,"Marketing","Lic Marketing y Publicidad")

institutoKhanamarka=[docente1,estudiante1,administrativo1]

for persona in institutoKhanamarka:
    print(persona.detalleRegistro())