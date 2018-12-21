from flask import Flask

app = Flask(__name__)
@app.route('/', methods=['GET'])
def api():
    return app.response_class(
        response="Eu Amo o Madeira",
        status=200,
        mimetype='application/json'
    )
