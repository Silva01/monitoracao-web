from flask import Flask
import os

app = Flask(__name__)
@app.route('/', methods=['GET'])
def api():
    complemento=os.environ['COMPLEMENTO']
    if complemento == "Teste":
        complemento = ""


    return app.response_class(
        response="Eu Amo o Madeira " + complemento,
        status=200,
        mimetype='application/json'
    )
