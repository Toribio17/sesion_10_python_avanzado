from flask import Flask
from flask_cors import CORS
from app.routes.ocr.controller import ocr_blueprint as ocr_class
from dotenv import dotenv_values,load_dotenv

app = Flask(__name__)
CORS(app)

app.register_blueprint(ocr_class)


#declarar variable de entorno
ENV = dotenv_values(".env")
load_dotenv(override=False)
print("Env: ",ENV)

@app.route('/', methods=['GET', 'POST'])
def hello():
    return "hello the services is working"
