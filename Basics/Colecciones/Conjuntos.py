#Conjuntos (Lista desordenada dode los elementos no se repiten)

conjunto = set() #Definir que es un conjunto vacio porque si no python piensa quie es un diccionario

conjunto = {} #Conjunto vacio

conjunto = {1,2,3,4.5,"Hola"} #No puede tener una colección dentro (lista o tupla)

conjunto.add(5)
conjunto.add("Adiós")

conjunto.discard(3) #Quitar elemento

conjunto.clear() 

print(conjunto)

print(3 in conjunto)
print(3 not in conjunto)

#Operaciones con conjuntos

a = {1,2,3} #Noes necesario el set ya que le estamos agregando elementos
b = frozenset({2,4,6}) #Hacer a B inmutable, no se pueden modificar sus elementos
d = {1,2,3,4,5}

print(a==b)
print(len(a))

c = a | b #Union de conjuntos
c = a & b #Intersección de conjuntos
c = a - b #Diferencia de conjuntos
c = a ^ b #Diferencia Simétrica

print(a.issubset(c)) #Si a es subconjunto de c
print(c.issuperset(a)) 
print(a.isdisjoint(b)) #Si no tienen ningún elemento en común
