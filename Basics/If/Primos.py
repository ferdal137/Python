#Detectar si un número es primo o no

import math

#Método 1

np = (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97)

num = int(input("Ingrese el número: "))

numsqrt = round(math.sqrt(num)) #Sirve per checar como redondear al más grande

for i in range(4):
    mod = numsqrt%np[i]
    if num==np[i]:
        print("El número es primo")
        break
    elif mod==0 and num!=np[i]:
        print("El número no es primo")





