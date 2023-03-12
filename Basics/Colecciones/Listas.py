#Listas

lista = ["lunes","Martes","Miercoles"]

print(lista[0])
print(lista[0:2]) #Muestra los elementos del índice 0 al 1
print(lista[-1])

print(len(lista)) #Número de elementos en la lista

#Insertar
listan = [1,2,4,5]
listan2 = [10,11,12]

listan.append(6) #Agrea elemento al final
listan.insert(2,3) #Agrega elemento en lugar especifico
listan.extend([7,8,9]) #Agrega un alista
listan[0] = 8 #Cambia el elemento que esta en ese indíce

listan3 = listan + listan2 #Suma de listas
print(listan)

print(4 in listan) #Si el elemento esta en la lista
print(listan.index(2)) #Muestra el índice del valor
print(lista.count(2)) #Cuantas veces aparece ese valor en la lista

#Eliminar
lista1 = [1,2,3,4,5,"Hola"]

lista1.pop(3) #Elimina elemento de la lista (índice)
lista1.remove("Hola") #Elimina elemnto de la lista
lista1.clear()

lista1.reverse()

lista1 = [1,4,8,6,5,3,2] * 3 #Se guardan tres veces los elementos

lista1.sort() #Ordena elementos ascendente
lista1.sort(reverse=True) #Ordena elementos descendente

lista = range(100)
lista = range(50,100)