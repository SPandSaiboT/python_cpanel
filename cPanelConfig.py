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
  
  
