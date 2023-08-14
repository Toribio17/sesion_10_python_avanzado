from flask import Flask
from flask_cors import CORS
from app.routes.ocr.controller import ocr_blueprint as ocr_class
from app.routes.status.controller import status_blueprint as ocr_status
from dotenv import dotenv_values,load_dotenv

app = Flask(__name__)
CORS(app)
app.debug = True

app.register_blueprint(ocr_class)

ENV = dotenv_values(".env")
load_dotenv(override=False)
print("Env: ",ENV)

@app.route('/', methods=['GET', 'POST'])
def hello():
    return "hello the services is working"
