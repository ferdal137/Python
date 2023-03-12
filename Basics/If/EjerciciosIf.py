"""
#Dos números par
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))

if n1%2==0 and n2%2==0:
    print("Los dos son par")
elif n1%2==0 and n2%2!=0:
    print("El primer número es par")
elif n1%2!=0 and n2%2==0:
    print("El segundo número es par")
else:
    print("Ningún número es par")

#Comparar tres números
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
n3 = int(input("Ingresa el tercer número: "))

if n1 > n2:
    if n1 > n3:
        print(n1,"es el número más grande")
    else:
        print(n3, "es el número más grande")
elif n2 > n3:
    print(n2, "es el número más grande")
else:
    print(n3, "es el número más grande")

#Vocales

letra = input("Digite una letra: ").lower()

if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
    print("La letra es una vocal")
else:
    print("La letra no es una vocal")

#Calculadora
num1 = float(input("Digite el primer número: "))
num2 = float(input("Digite el segundo número: "))
ope = input("Qué operación desea realizar: ").lower()
res = 0

if ope=='s':
    res = num1 + num2
    print("El resultado de la suma es: ", res)
elif ope=='r':
    res = num1 - num2
    print("El resultado de la resta es: ", res)
elif ope=='p' or ope=='m':
    res = num1 * num2
    print("El resultado de la multiplicación es: ", res)
elif ope=='d':
    res = num1 / num2
    print("El resultado de la división es: ",res)
else:
    print("Operación no reconocida")

#Cajero automático
saldo = 1000
print("Buenas tardes\nBienvenido a BBVA Bancome\nSu saldo en la cuenta es de: $", saldo)
print("Digite el número de la operación que desea realizar: ")
print("1. Ingresar dinero en la cuenta\n2. Retirar dinero de la cuenta\n3. Mostrar dinero disponible\n4. Salir")
ope = int(input())
if ope==1:
    ing = int(input("Cúanto dinero desea ingresar:\n"))
    saldo = saldo + ing
    print("Su nuevo saldo es de: $", saldo)
elif ope==2:
    ing = int(input("Cúanto dinero desea retirar:\n"))
    saldo = saldo - ing
    print("Su nuevo saldo es de: $", saldo)
elif ope==3:
    print("Su saldo en la cuenta es de: $",saldo)
elif ope==4:
    print("Vuelva pronto")"""

#Mayor de edad en una linea

print("Eres mayor de edad" if  int(input("Ingresa tu edad"))>=18 else "No eres mayor de edad")


