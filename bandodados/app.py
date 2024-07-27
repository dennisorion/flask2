from flask import Flask, request, jsonify, abort
from models import Pessoa, Veiculo, session

app = Flask(__name__)



@app.route('/pessoa/<string:nome>', methods=["GET"])
def get_idade_pessoa(idade):

    pessoa = session.query(Pessoa).filter_by(idade=idade).first()

    return pessoa.nome



if __name__ == "__main__":
    app.run(debug=True)