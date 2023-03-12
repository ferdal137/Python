#Bucle while

import math

numero = int(input("Digite un número positivo"))

while numero<0 :
    print("Error \n El número debe de positivo")
    numero = int(input("Digite otro número: "))

print(f"La raíz cuadrada es: {(math.sqrt(numero)):.2f}")

i = 0

while i<11:
    print("Hola Mundo")
    i += 1