###codigo 1 suma de una lista 
lista = [3,5,7,9,11]
total = 0
for i in lista:
    total=total+i
print("la suma total de la lista es:",total)


###codigo 2 numero par o impar
numero = int(input("ingrese un numero entero:")) 

if numero % 2 == 0:
    print("el numero es par")

else:
    print("el numero es impar")
    

###codigo 3 tabla de multiplicar
numero = int(input("ingrese un numero "))

for i in range(0,11):
    resultado = i * numero
    print(numero,"X",i,"=",resultado)


###codigo 4 promedio de una lista
lista = [4,6,8,10,12]
suma=sum(lista)
print(f"el resultado de la suma es:{suma}")

numeros = len(lista)
print(numeros)

promedio = sum(lista) / len(lista)
print(f"el promedio de la lista es:{promedio}")


###codigo 5 contar vocales 
frase = input("ingrese una palabra:")
contador = 0
for i in frase:
    if i in "aeiou":
        contador = contador+1
print(f"la palabra que ingresaste tiene {contador} vocales")


###codigo 6 invertir una cadena
cadena = input("ingrese una palabra: ")

cadena_invertida = ""

for caracter in cadena:
    cadena_invertida = caracter + cadena_invertida

print("la cadena invertida es:",cadena_invertida)

###codigo 7 numeros pares en un rango 
for i in range(1,50):
    if i %2 == 0:
        print(i)
    






