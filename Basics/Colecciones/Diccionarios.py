#Diccionarios

diccionariov = {} #Diccionario vacio

print(diccionariov)

diccionario = {"azul":"blue","rojo":"red","verde":"green"}

print(diccionario["rojo"]) #Se mostraría red

diccionario["Amarillo"] = "Yellow" #Agregar elementos o modificar elementos

del(diccionario["verde"]) #Eliminar elementos

equipo = {10:"Messi",7:"Ronaldo",11:"Pogba"}

print(equipo[10]) #No es el índice es el jugador con al número 10 el que va a mostrar
print(equipo.get(9,"El jugador no esta en el equipo")) #No se marca error, muestra el texto en caso de no encontara el elemento
print(10 in equipo)
print(equipo.keys()) #Muestra solo las claves
print(equipo.values()) #Muestra solo los valores de las claves
print(equipo.items()) #Muestra las claves y sus valores en tuplas
print(len(equipo)) #Cuantos jugadores hay en el equipo

equipo.clean() #Se vacia el diccionario