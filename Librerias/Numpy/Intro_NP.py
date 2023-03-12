import numpy as np
import sys #Time y memory

 #Creamos la matriz de una dimensión
a = np.array([(1,2,3)])
print("1D array = ", a)

#Creamos la matriz de dos dimensiones
b = np.array([(1,2,3),(4,5,6)]) 
print('2D array = \n', b)
print(a.ndim) #Dimensión de la matriz
print(a.dtype) #Tipo de dato que contiene la matriz
print(a.size) #Número de elementos
print(a.shape) #Forma (1 dimensión, 3 elementos)

#Matriz solo con unos (alto,largo)
unos = np.ones((3,4)) 
print(unos)

#Matriz con puros ceros
ceros = np.zeros((3,4)) 
print(ceros)

#Matriz con números aleatorios
aleatorios = np.random.random((2,2)) 
print(aleatorios)

#vacia = np.empty((3,2)) #Matriz Vacia
#print(vacia)

#Matriz de un solo valor
one_value = np.full((2,2),8) 
print(one_value)

#Matriz con suceción (0,5,10,...,30)
suces = np.arange(0,30,5) 
print(suces)

#Matriz de n valores con sucesion cada 2/n
esp = np.linspace(0,2,5) 
print(esp)

#Matriz identidad
identidad1 = np.eye(4,4) 
print(identidad1)

#Matriz identidad
identidad2 = np.identity(4) 
print(identidad2)

#Cambio de forma
c = np.array ([(8,9,10),(11,12,13)]) #Creamos matriz 2 x 3
print(c)
c = c.reshape(3,2) #Cambiamos a una matriz 3 x 2
print(c)

#Seleccionar un solo elemento
print(c[0,1]) #Nos muestra el segundo elemento del primer vector
print(c[0: ,1]) #Nos muestra el segundo elemento de todas las filas 

#Operaciones matemáticas entre matrices

d = np.array([2,4,8])

print(d.min()) #Valor mínimo = 2
print(d.max()) #Valor máximo = 8
print(a.sum()) #Suma de los elementos
print(np.sqrt(d)) #Raiz cuadrada de cada elemento
print(np.std(d)) #Desviación estandar entre los elemntos

x = np.array([(1,2,3),(3,4,5)])
y = np.array([(1,2,3),(3,4,5)])

print(x + y)
print(x - y)
print(x * y)
print(x / y)
