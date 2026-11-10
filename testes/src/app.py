# app.py
from flask import Flask, jsonify, request


def create_app():
    app = Flask(__name__)
    app.config['TESTING'] = True  # Ativa o modo de teste (melhora logs de erro)
 
    @app.route('/api/saudacao', methods=['GET'])
    def saudacao():
        return jsonify({"mensagem": "Olá, Mundo!"})
 
    @app.route('/api/soma', methods=['POST'])
    def soma():
        dados = request.get_json()
        resultado = dados['a'] + dados['b']
        return jsonify({"resultado": resultado})
 
    return app
 
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)