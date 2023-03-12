###Entornos virtuales  

[comment]: <> (Para abrir el visualizador presionar ctrl+k+v)

Un entorno virtual es una carpeta con diferentes paquetes (librerias) que se
utilizaran en un proyecto determinado, ya que si en algún futuro necesitamos 
modificar algo de ese proyecto debemos hacerlo con la version del paquete
que se usó para desarrollarlo; es por eso que los paquetes se guardan en el 
entorno virtual con su versión especifica para que esta no se actualice.

####Creación de Entornos virtuales en python

```python

>>>Primero accedemos a la carpeta donde queremos crear nuestro entorno virtual

>>>python -m venv nombre-env #Crear el entorno virtual (carpeta)

>>>cd nombre-env\Scripts #Entramos a la carpeta de Scripts

>>>activate.bat #Activamos el entorno virtual

>>>cd nombre-env #Regresamos a la carpeta principal

>>>pip install modulo #Instalamos el modulo
```
