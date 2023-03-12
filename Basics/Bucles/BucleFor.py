#Bucle For

coleccion = [1,2,3,4,5]

for i in coleccion:
    print("HolaMundo")

dicc = {22:10,21:12,20:13}

for clave, valor in dicc.items():
    print(f"{clave} ---> {valor}")

cadena = "Fernando"

for i in cadena:
    print(f"{i}",end = " ")

#For tipo range

for i in range(10):
    print(i)

for i in range(5,11):
    print(i)

for i in range(2,21,2):
    print(i)