#Ejercicio 1 
"""
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

a1 = len(palabra1)
a2 = len(palabra2)

if a1>a2 :
    print(f" {palabra1} es la palabra más grande")
elif a1<a2:
    print(f" {palabra2} es la palabra más grande")
elif a1==a2:
    print("Las dos palabras son iguales")

#Ejercicio 2

palabra = input("Ingrese una frase con punto o sin el: ")

if palabra.endswith("."):
    print("La palabra términa con un punto")
else:
    print("La palabra no términa con punto")

#Ejercicio 3

palabra = input("Ingrese la palabra o frase: ").lower()

palabra = palabra.replace(" ","")

palabrar = palabra[::-1]

if palabra == palabrar:
    print("La palabra es palíndroma")
else:
    print("La palabra no es palíndroma")

#Ejercicio 4

frase = input("Ingrese la frase: ").lower()

frase = frase.replace(" ","*")

frase = frase.title()

print(frase) """

#Ejercicio 5

palabra = input("Ingrese la frase: ").lower()

print("Hay", palabra.count("a"), "letras a en la palabra")
print("Hay", palabra.count("e"), "letras e en la palabra")
print("Hay", palabra.count("i"), "letras i en la palabra")
print("Hay", palabra.count("o"), "letras o en la palabra")
print("Hay", palabra.count("u"), "letras u en la palabra")

