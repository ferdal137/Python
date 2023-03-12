#Tuplas

tupla = (1,2,3,4,5)
lista = list(tupla) #Convertir a lista

lista1 = ["a","b","c","d","e"]
tupla1 = tuple(lista1) #Convertir a tupla

print(tupla)
print(tupla[0])
print(tupla[0:2]) #Muestra los elementos del índice 0 al 1
print(tupla[-1])

print(1 in tupla)
print(tupla.index(3)) #En que indice esta el 3
print(tupla.count(3)) #Cuantas veces esta el 3
print(len(tupla)) #Cuantos elementos hay en mi tupla