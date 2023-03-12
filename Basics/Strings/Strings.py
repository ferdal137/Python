#Strings

cadena = "Estoy \"estudiando\""
cadena = "Estoy \testudiando" #Añade 4 espacio (Tabulador)
cadena = "Estoy \nestudiando" #Salto de linea
cadena = 'D:\nombre\trabajo' #Datos en crudo (tal cual estan) si en el print añadimos raw_cadena
cadena = """ Hola
Que tal?
Mi nombre es Fernando
"""

cadena1 = "Hola"
cadena2 = "Mundo"

#print(raw_cadena)
print(cadena1 + cadena2) 

cadena123 = "Fernando"

print(cadena123[0]) #Muestra la letra en el índice 0
print(cadena123[:3]) #Muestra las letras del índice 0 al 2

cadena123[7] = 'a' #Error ya que las litas son inmutables
cadena123 = "f" + cadena123[1:]

print(len(cadena123)) #Calcula el número de caracteres de una cadena

#Métodos

cadenaM = "Hola Mundo".upper() #Convierte la cadena a mayusculas
cadenaM = "Hola Mundo".lower() #Convierte la cadena a minusculas
cadenaM = "Hola Mundo".capitalize() #Primera letra en Mayuscula
cadenaM = "Hola Mundo".title() #Primera letra de cada palabra en mayuscula
cadenaM = "Hola Mundo".count('o') #Contar caracteres o palabras
cadenaM = "Hola Mundo".find('H') #Regresa el índice del caracter o de la palabra
cadenaM = "Hola Mundo".rfind('H') #Busca el ultimo índice
cadenaM = "100000".isdigit() #Si tiene solo números o no
CadenaM = "ABCDEF".isalpha() #Si tiene solo letras o no
CadenaM = "ABCDEF12345".isalnum() #Si tiene caracteres alfa-numéricos
cadenaM = "HOLA MUNDO".isupper()
cadenaM = "hola mundo".islower()
cadenaM = "Hola Mundo".istitle() 
cadenaM = "        ".isspace() #True
cadenaM = "Hola Mundo".startswith("h") #True or False si inicia con:
cadenaM = "Hola Mundo".endswith("h")
cadenaM = "Hola Mundo".split() #Separa las palabras y las pone en una lista
cadenaM = "Hola-Mundo".split("-") 
cadenaj = ",".join("Fernando") #Separa cada uno de los elementos de mi cadena
cadenaM = "     H     ".strip() #Elimina espacios
cadenaM = ".....H.....".strip(".")
cadenaM = "Hola Mundo".replace("o","0") #Remplaza elementos