
def verificandoEdad (edad):
    if edad<0:
        raise ValueError ("La edad no puede ser negativa")
    elif edad<18:
        print("Eres menor de edad")
    elif edad>115:
        raise ValueError ("Ingrese una edad valida")
    else:
        print("Eres mayor de edad")

edadUser = int(input("Ingrese su edad: "))

try:
    verificandoEdad(edadUser)

except ValueError as EdadNoValida:
    print("La edad no es valida") 


print("Programa termiando")