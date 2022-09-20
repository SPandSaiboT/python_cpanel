from flask import Flask
from flask import render_template
import os
from dotenv import load_dotenv

#Carga variables de entorno
load_dotenv()
debugENV = os.getenv('DEBUG_MODE')
portENV = os.getenv('PORT')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('/index.html')
  
  
# INICIO APP
if __name__ == '__main__':
    app.run(debug=debugENV, port=portENV)
