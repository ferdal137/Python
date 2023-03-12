#Ejercicio 1

"""lista = [1,2,3,4,"Hola","Adios",3,1,1,1,"Hola"]

conjunto = set(lista)

lista = list(conjunto)

print(lista)

#Ejercicio 2

lista1 = {1,2,3,4,5,6,7,8,9}
lista2 = {2,4,6,8,10,12,14,16}

print(lista1)
print(lista2)

conjunto1 = set(lista1)
conjunto2 = set(lista2)

list1 = list(conjunto1 & conjunto2)
list2 = list(conjunto1 - conjunto2)
list3 = list(conjunto2 - conjunto1)
list4 = list(conjunto1 | conjunto2)

print(list1)
print(list2)
print(list3)
print(list4) """

#Ejercicio 3

lista = []

p1 = {"Nombre":"Aragorn","Clase":"Guerrero","Raza":"Dúnadan del Norte"}
p2 = {"Nombre":"Gandalf","Clase":"Mago","Raza":"Istar"}
p3 = {"Nombre":"Legolas","Clase":"Arquero","Raza":"Elfo Sindar"}

lista.append(p1)
lista.append(p2)
lista.append(p3)

print(lista)
