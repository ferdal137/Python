#Funciones sin retotorno de valor

def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Fernando")
saludar("Alejandro")

def TablaDeMultiplicar (num):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")

TablaDeMultiplicar(5)
print()
TablaDeMultiplicar(10)

#Funciones con retorno de valor

def multiplicar (n1,n2):
    valor = n1 * n2
    return valor

print(multiplicar(3,5))

mult = multiplicar(3,5)

print(mult)

print(multiplicar(7,8))

def prueba():
    return "Hola",9999,[1,2,3,4]

print(prueba())

s,i,l = prueba()

print(s)
print(i)
print(l)