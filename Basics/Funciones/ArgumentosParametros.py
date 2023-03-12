#Argumentos y paramétros

def restar (n1,n2): #Parámetros
    return n1-n2

print(restar(4,3)) #Argumentos
print(restar(n2=4,n1=3))

#Argumentos por valor o por referencia

def doblar_valor(numero):
    return numero*2
    
n = 5
n = doblar_valor(n)

print(n)

def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

n = [1,2,3,4,5]
doblar_valores(n)
doblar_valores(n[:]) #Para que se pase una copia y no modifique la variable original

print(n) #Las colecciones se modifican con la función