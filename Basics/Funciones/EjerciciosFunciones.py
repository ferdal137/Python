#Ejercicio 1
"""
def Pesos_Dolares(pesos):
        print(f"{pesos} pesos son {pesos*0.050} dolares")

def Dolares_Pesos(dolares):
        print(f"{dolares} dolares son {dolares*19.97} pesos")
        
while True:
    #Faltan 3 comillas print(.:MENU:.
 1.- Convertir Pesos Mexicanos a Dolares
 2.- ConvertirDolares a Pesos Mexicanos
 3.-Salir #Faltan 3) 

    option = int(input("Ingrese el número de la operación a realizar: "))

    if option == 1:
        p = int(input("Ingrese la cantidad de pesos a convertir: "))
        Pesos_Dolares(p)
    elif option == 2:
        d = int(input("Ingrese la cantidad de dolares a convertir: "))
        Dolares_Pesos(d)
    else:
        exit() 

#Ejercicio 2

alto = int(input("Ingrese el alto del rectangulo: "))
largo = int(input("Ingrese el largo del rectángulo: "))

def dibujarR (alto,largo):
    for i in range(0,alto):
        print(("*")*largo)

dibujarR(alto,largo) 

#Ejercicio 3

dicc = {"Juan López":123,"Pedro Páramo":987,"Jorge Jiménez":765}


def agregar(nombre,iden):
    dicc[nombre] = iden
    print("Cliente agregado")

def mostrar():
    print("La lista de clientes es: ")
    print(dicc.keys())

def mostrarPorID(iden):
    print(list(dicc.keys())[list(dicc.values()).index(iden)])

def eliminar(nombredel):
    del(dicc[nombredel])
    print("El nombre se ha eliminado")
    print(dicc)

while True:
    print(#Agregar 3 comillas.:MENU:.
 1.- Agregar nuevo cliente
 2.- Mostrar todos los clientes
 3.- Mostrar cliente por DNI
 4.- Eliminar cliente
 5.- Salir #Agregar 3 comillas) 

    option = int(input("Ingrese el número de la operación a realizar: "))

    if option == 1:
        nombre = input("Ingrese nombre: ")
        iden = int(input("Ingrese ID: "))
        agregar(nombre,iden)
    elif option == 2:
        mostrar()
    elif option == 3:
        iden = int(input("Ingrese el ID: "))
        mostrarPorID(iden)
    elif option == 4:
        nombredel = input("Ingrese el nombre que desee eliminar: ")
        eliminar(nombredel)
    else:
        exit() 
    
#Ejercicio 4

def factorial(num):
    if num>0:
        resultado = num *  factorial(num-1)
    else:
        resultado = 1

    return resultado

print(factorial(int(input("Ingrese el número: "))))"""

#Ejercicio 5

def sumar_numeros(num):
    if num==0:
        resultado = 0
    else:
        resultado = sumar_numeros(int(num/10)) + (num%10)
    
    return resultado

valor = sumar_numeros(123)

print(valor)

