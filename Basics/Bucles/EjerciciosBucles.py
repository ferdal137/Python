#Ejercicios Bucles

"""#Ejercicio1

lista = []

lista = list(range(1,51)) #Añadir los elementos en la lista en una sola linea

i = 1

while i<=50:
    lista.append(i)
    i += 1

i = 0

for i in lista:
    print(i,end = "-")

#Ejercicio 2

lista = list(range(1,11))

numero = int(input("Digite un número: "))

indice = 0

for i in lista:
    mult = i * numero
    lista[indice] = mult
    indice += 1

print(lista)

#Ejercicio 3

lista = []

n = 1

salir = False 

while not salir:
    n = int(input("Inserte un número: "))
    if n==0:
        salir = True
    else:
        lista.append(n)

lista.sort()

print(lista)

#Ejercicio 4

n1 = int(input("Ingrese el rango:\n "))
n2 = int(input("---->\n "))

n2 += 1
suma = 0
v = 0

if n1%2!=0:
    n1 += 1

for i in range(n1,n2,2):
    v = suma
    suma = v + i

print("El resultado de la suma es:", suma)

#Ejercicio 5

num = int(input("Ingrese un número positivo: "))

while num<=0:
    print("El número debe de  ser prositivo")
    num = int(input("Ingrese un número positivo: "))

factorial = 1


for i in range(1,num + 1):
    
    factorial *= i

print(f"El factorial de {num} es: {factorial} ")


#Ejercicio 6

n = int(input("Ingrese un número: "))

lista = []

for i in range(1,11):
    lista.append(i * n)

print(lista) 

#Ejercicio 7

import random

aleatorio = random.randint(0,100)

intento = 0 

n = int(input("Ingrese un número: "))

while aleatorio!=n:
    if n==aleatorio:
        print("Felicidades a adivinado el número al primer intento")
    elif n>aleatorio:
        print(f"{n} es mayor que el número")
        n = int(input("Ingrese un número: "))
        intento += 1
    elif n<aleatorio:
        print(f"{n} es menor que el número")
        n = int(input("Ingrese un número: "))
        intento += 1
print(f"Felicidades a adivinado el valor del número despues de {intento} intentos")
"""

#Ejercicio 9

frase = input("Ingrese una frase: ")
