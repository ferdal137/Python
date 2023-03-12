import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

boston = datasets.load_boston()
#print(boston)

print("Información del dataset: ")
print(boston.keys())

print("Características del dataset: ")
print(boston.DESCR)

print("Cantidad de datos: ")
print(boston.data.shape)

print("Nombres columnas: ")
print(boston.feature_names)

x = boston.data[:, np.newaxis, 5]

y = boston.target

plt.scatter(x,y)
plt.xlabel("Número de habitaciones")
plt.ylabel("Valor Medio")
plt.show()

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split (x, y, test_size=0.2)

lr = linear_model.LinealRegression()

lr.fit(x_train,y_train)

Y_pred = lr.predict(x_test)

plt.scatter(x_test,y_test)
plt.plot(x_test, Y_pred, color = "red", linewidth = 3)
plt.tittle("Regresión lineal simple")
plt.xlabel("Número de habitaciones")
plt.ylabel("Valor Medio")
plt.show()

