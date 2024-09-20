#CLASE AUTO

class Auto:
    def __init__(self,color, marca,modelo):
        self.color=color
        self._marca=marca
        self._modelo=modelo
    
    #Metodos o acciones
    def caracteristicas(self):
        return f"Auto: {self._marca} - modelo: {self._modelo}"

class VehiculoElectrico(Auto):
    def __init__(self,color,marca,modelo,bateria):
        super().__init__(color,marca,modelo)
        self._bateria=bateria
    def caracteristicas(self):
        return super().caracteristicas()+f" Tipo de Bateria: {self._bateria}"

class Vehiculo(Auto):
    def __init__(self,color,marca,modelo,combustible):
        super().__init__(color,marca,modelo)
        self._combustible=combustible
    
    def caracteristicas(self):
        return super().caracteristicas()+f" Combustible: {self._combustible}"
    

def caracteristicasAuto(auto):
    return auto.caracteristicas()

##Creacion de los objetos de la clase

auto1=VehiculoElectrico("Rojo","Quantum",2024,"Litio 60V")
auto2=Vehiculo("Azul","Toyota", 2024,"Gasolina")

#Describir los vehiculos

print("Autos Electricos")
print(caracteristicasAuto(auto1))

print("Autos a Gasolina")
print(caracteristicasAuto(auto2))