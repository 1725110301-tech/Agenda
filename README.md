# Bootstrap webapp
Ejercicios de Aplicaciones Web con Python3, SQlite3 y web

# 1. Crear un ambiente virtual (Virtual Eviroment)
Crear el Virtual Eviroment para la instalacion de las librerias necesarias para el proyecto.
````shell
python3 -m venv .venv
````
# 2. Crear el archivo .gitignore
crear el archivo **.gitignore** para configurar los recursos que necesitamos que se sincronicen con el repositorio

````sell
*.pyc
__pycache__/
.venv/
````
# 3. Activar el virtual environment
Activar el **Virtual Environment** para realizar la instalacion de librerias necesarias
````shell
source .venv/bin/activate
````

# 4. Actualizar  **PIP**
Actualizar el instalador de paquetes de python **pip**

````shell
pip install --upgrade pip
````

# 5. Crear el archivo **runtime.txt**
Crear el archivo **runtime.txt** con la versión utilizada de python3
````shell
pyhon3 -V > runtime.txt
````

# 6. Instalar el micro-framework **web.py**
Instalar el micro-framework **web.py** en el ambiente virtual 
````shell
pip install web.py
````
## 7. Crear el archivo **requirements.txt.
Crear el archivo **requirements.txt** con las versiones de las libnrerias instaladas en el ambiente vitrual

````shell
pip freeze > requirements.txt
````

## 8. Indexar el contenido del repositorio
Indexar todo el contenido del repositorio para incluiir todos los archivos nuevos y las modificaciones realizadas al código

````shell
git add .
````

## 9. Crear el **commit** o el punto de control
Crear un punto de control(**commit**)con los cambios al proyecto

````shell
git commit -m "CREATED configuración del ambiente virtual"
````

## 10. Realizar un push hacia el repositorio

Realizar un **push** hacia el repositorio para sincronizar los cambios realizados en el proyecto

````shell
git push -u origin main
````