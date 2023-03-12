
def dividir():
    while True:
        try:
            num1 = float(input("Digite el primer número: "))
            num2 = float(input("Digite el segundo número número: "))
            resultado = num1/num2

        except ValueError:
            print("Error --> Digite correcrtamente los números")

        except ZeroDivisionError:
            print("Error --> No se puede dividir entre cero")
        
        else:
            break

dividir()