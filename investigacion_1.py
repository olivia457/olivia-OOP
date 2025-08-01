###codigo 8 mayor de tres numeros

n1 = int(input("ingrese el primer numero: "))
n2 = int(input("ingrese el segundo numero: "))
n3 = int(input("ingrese el tercer numero: "))

if n1 >= n2 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
else:
    mayor = n3
print(f"el numero mayor es: {mayor}")


###codigo 9 suma de digitos

numero = (input("ingrese un numero entero: "))

suma = 0
for digito in numero:
    suma = suma + int(digito)
print(f"la suma de los difitos es: ",suma)


    
###codigo 10 contador de palabras

def contador_de_palabras (texto):
    palabras = texto.split()
    cantidad_de_palabras = len(palabras)
    return cantidad_de_palabras
    
frase = input("ingrese una frase: ")
resultado = contador_de_palabras(frase)
print(f"el numero de palabras es: ", resultado)



###codigo 11 lista inversa

lista = [1,2,3,4,5,6,7,8,9,10]

def invertir_lista(lista):
    if lista == []:
        return lista
    else:
        return [lista[-1]] + invertir_lista(lista[:-1])
print(invertir_lista(lista))


#codigo 12 numeros aleatorios

from random import randint
lista = [randint(1,20) for i in range(0,5)]
print(lista)
    


###codigo 13 adivinar numeros

import random

numero_secreto = random.randint(1,10)

while True:

    intento = int(input("ingresa tu intento: "))

    if intento < numero_secreto:
        print("pista: el numero es mayor")
        
    elif intento > numero_secreto:
        print("pista: el numero es menor")
        
    else:
        print("¡felicidades adivinaste el numero")
        
        


###codigo 14 secuencia personalizada

def lista_de_multiplos(inicio,final):

    multiplos = []

    for numeros in range(inicio,final +1,inicio):

        multiplos.append(numeros)
    
    return multiplos

print(lista_de_multiplos(3,30))





    
    



