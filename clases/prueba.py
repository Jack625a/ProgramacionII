print("Programacion II")
#1. tipos datos
#1.1 Numericos
numero=15
numero2=10.5
#1.2. Cadenas de caracteres
nombre="Kevin"
nombre2='Kevin Arroyo'
#1.3. Booleanos
encender=False
#variables

#condicionales
#if
if numero<numero2:
    print(numero,"es menor que", numero2 )
else:
    print(numero2,"es menor que", numero)
#bucles
n=1
while n<=numero:
    print(n)
    n=n+1

#Bucles iterativos - rango
for i in range(1,16):
    print(i)
#funciones
def sumar(a,b):
    return (a+b)

print(sumar(numero,numero2))
print(sumar(5,9))