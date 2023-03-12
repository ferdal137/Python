import pandas as pd 
import numpy as np

#Creación de un dataframe
data = np.array([("","Col1","Col2"),("Fila1",11,22),("Fila2",33,44)])
print(pd.DataFrame(data=data[1:,1:], index=data[1:,0], columns=data[0,1:] ))

df = pd.DataFrame([(1,2,3),(4,5,6),(7,8,9)])
print("DataFrame:\n",df)

#Creación de Series
series = pd.Series({"Argentina":"Buenos Aires",
                    "Chile":"Santiago de Chile",
                    "Colombia":"Bogotá",
                    "Peru":"Lima"
})

print(series)

#Exploración
print(df.shape) #Forma de los Datos (Matriz 3x3)
print(len(df.index)) #Altura del DataFrame
print(df.describe()) #Estadísticas del DataFrame
print(df.mean()) #Medida de las columnas
print(df.corr()) #Correlación
print(df.count()) #Conteo de datos del DataFrame
print(df.max()) #Valor más alto de cada columna
print(df.min()) #Valor más bajo de cada columna
print(df.median()) #Promedio de cada columna
print(df.std()) #Desviación estandar de cada columna

#Selección
print(df[0]) #Seleccionar columna
print(df[[0,1]]) #Seleccionar dos columnas
print(df.iloc[0][2]) #Seleccionar valor (fila,columna)
print(df.loc[0]) #Seleccionar fila y mostrarla como columna
print(df.iloc[0,:]) #Otra forma seleccionar fila

#Limpieza
print(df.isnull()) #True si faltan valores en las celdas
print(df.isnull().sum()) #Contador de valores nulos 
df.dropna() #Eliminar filas con valores nulos
df.dropna(axis=1) #Eliminar las columnas con valores nulos
df.fillna() #Remplaza los valores perdidos con algún dato que indiquemos
df.fillna(df.mean()) #Remplazar con el promedio de los demás datos

