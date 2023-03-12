#Excepciones

while True:
    try:
        numero = int(input("Digite un número: "))
        print(numero)

    except:
        print("Ha ocurrido un error")

    else:
        print("Programa finalizado correctamente")
        break

    finally:
        print("Iteración finalizada")


print("Programa finalizado")