# python_cpanel


## Paso 1 
- Crear capeta para proyecto
- Crear entorno virtual
	- Ejecutar en consola
		  virtual env env_tutorial
	- Activar virtual env
	- instalar dependencias
		  pip install python-dotenv
- Abrir proyecto en VisualStudio
- Crear Carpetas y archivos (cmd|vscode)
- Cerar app en flask (Documentacion | o tipeado)
- Crear template
	index.html
	- integrar CND de bootstrap

			<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
			<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
	
	
		<!DOCTYPE html>
		<html lang="en">
		  <head>
			<meta charset="UTF-8" />
			<meta http-equiv="X-UA-Compatible" content="IE=edge" />
			<meta name="viewport" content="width=device-width, initial-scale=1.0" />
			<link
			  href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css"
			  rel="stylesheet"
			  integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT"
			  crossorigin="anonymous"
			/>

			<title>Test Python on cPanel</title>
		  </head>
		  <body>
			<div class="container">
			  <h1>Hola cPanel !</h1>
			  <div class="row">
				<div class="col-md-4">
				  <h2>Deploy en cPanel</h2>
				</div>
				<div class="col-md-4">
				  <h2>... OK !</h2>
				</div>
				<script
				  src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"
				  integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8"
				  crossorigin="anonymous"
				></script>
			  </div>
			</div>
		  </body>
		</html>

## Paso 2 
- Crear .ENV con variable de entorno
- Crear carpeta lib en directorio
- Crear cPanelConfig.py en lib
  - Codigo:
   
		import os
		try:
		  os.system('pip install pip install python-dotenv')  
		  os.system('pip install --upgrade pip')
		  os.system('pip install flask')
		  with open("passenger_wsgi.py", "w") as f:
			 f.write("from app import app as application")
			 f.close()
		  print('passanger_wsgi MOD OK !')
		  print("Configuracion completa !")  
		except Exception as e:
		  print("Oops!", e.__class__)
		  print("Revisa e intenta de nuevo")
  
- Crear carpeta setup
- Crear archivo requirements.py
  - Codigo:

		import os
		os.system('pip install pip install python-dotenv')
    
- Crear archivo runScript.py
  - Codigo:

		import os
		from dotenv import load_dotenv
		load_dotenv()
		scrpt = os.getenv('SCRIPT')
		os.system(scrpt)
    
- Crear archivo setup.py
  - Codigo:

		import requirement 
		import runScript

		def setup():
		  print('Setup OK!')
		if __name__ == '__main__':
		  setup()

## Paso 3
- Crear zip

## paso 4
- Crear aplicacion en cPanel
	- Application Root -> Nombre de la carpeta donde se alojaran los archivos
	- Application URL -> URL accesible del proyecto
	- Application entry point -> ruta raiz de la aplicacion
	- Application startup file -> nombre del archivo que correo la aplicacion
	- CreateAPP
- Agregamos Variables de entorno:

	DEBUG_MODE	False
	PORT	4000
	SCRIPT	Comando que se crea con la app

- Subir Archivos
- Ruta de archivos
		/home/demosspa/cpython/
    - Descomprimir
- Correr scripts
	- Desde el cPanel->python->App
	
		/home/demosspa/cpython/setup/setup.py
		/home/demosspa/cpython/cPanelConfig.py

Restart app
Visitar Link
