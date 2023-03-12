#Pilas

pila = [1,2,3]

pila.append(4) #Se agrega al final
print(pila)

n = pila.pop() #Quita el elemento del final y lo guarda en n
print(pila)


#Colas

cola = ["Maria","Jose","Alejandro"]

cola.append("Karla") #Agregamos un elemento al final de la cola
cola.append("Flor")

print(cola)

n = cola.pop(0) #Quitamos el elemento del inicio de la cola y lo guardamos en n

print("Atendiendo a",n)