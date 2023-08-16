from flask import Flask
from flask_cors import CORS
from app.routes.ocr.controller import ocr_blueprint as ocr_class
from app.routes.manage_people.contoller import people_blueprint
from dotenv import dotenv_values,load_dotenv

app = Flask(__name__)
CORS(app)

app.register_blueprint(ocr_class)
app.register_blueprint(people_blueprint)

#declarar variable de entorno
ENV = dotenv_values(".env")
load_dotenv(override=False)
print("Env: ",ENV)

@app.route('/', methods=['GET', 'POST'])
def hello():
    return "hello the services is working"
