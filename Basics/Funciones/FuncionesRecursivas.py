#Funciones Recursivas

def cuenta_regresiva(num):
    if num>0:
        print(num)
        cuenta_regresiva(num-1)
    else:
        print("BOOM")

cuenta_regresiva(int(input("Ingrese un número: ")))
