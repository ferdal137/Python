import matplotlib.pyplot as plt

"""#Diagrama de linea
x1 = [1,2,3,4]
x2 = [11,22,33,44]
y1 = [3,4,5,6]
y2 = [44,33,22,11]

plt.plot(x1, x2, label = "Linea 1", color = "blue", linewidth = 3)
plt.plot(y1, y2, label = "Linea 2", color = "green", linewidth = 3)

plt.title("Diagrama de líneas")
plt.ylabel("Eje y")
plt.xlabel("Eje x")

plt.legend() #Mostrar leyenda
plt.grid() #Mostrar cuadricula
plt.show() #Mostrar gráfica

#Gráfica de barras
x1 = [.25,1.25,2.25,3.25,4.25]
y1 = [10,55,80,32,40]
x2 = [.75,1.75,2.75,3.75,4.75]
y2 = [42,26,10,29,66]

plt.bar(x1, y1, label = "Datos 1", color = "blue", width = .5)
plt.bar(x2, y2, label = "Datos 2", color = "orange", width = .5)

plt.title("Gráfico de barras")
plt.ylabel("Eje y")
plt.xlabel("Eje x")

plt.legend() 
plt.show() 

#Histogramas
a = [22,33,40,65,32,45,15,4,2,102,115,130,98,100,67,45,39]
bins = [10,20,30,40,50,60,70,80,90,100]

plt.hist(a, bins, histtype = "bar", rwidth = 0.8, color = "green" )

plt.title("Histograma")
plt.ylabel("Eje y")
plt.xlabel("Eje x")

plt.show() 

#Gráficos de dispersión
x1 = [.25,1.25,2.25,3.25,4.25]
y1 = [10,55,80,32,40]
x2 = [.75,1.75,2.75,3.75,4.75]
y2 = [42,26,10,29,66]

plt.scatter(x1, y1, label = "Datos 1", color = "red")
plt.scatter(x2, y2, label = "Datos 2", color = "purple")
plt.title("Gráfico de dispersión")
plt.ylabel("Eje y")
plt.xlabel("Eje x")

plt.legend() 
plt.show() """

#Gráfico circular
dormir = [8,9,10,15]
comer = [2,4,3,5]
trabajar = [4,6,7,5]
recreacion = [7,8,4,10]
divisiones = [7,2,2,7]
actividades = ["Domir","Comer","Trabajar","Recreación"]
colores = ["red","purple","blue","orange"]

plt.pie(divisiones, labels = actividades, colors = colores, 
        startangle = 90, shadow = True, explode = (0.1,0,0,0), autopct = "%1.1f%%")

plt.title("Gráfico circular")

plt.show()