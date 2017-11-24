from flask import Flask, jsonify, abort, make_response
from flask import request

from flasgger import APISpec, Schema, Swagger, fields

version = 0.1

app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'Pessoas API RESTful',
    'uiversion': 2,
    'version':version
}
swagger = Swagger(app)

pessoas = [
    {
        'id': 1,
        'nome': 'Fernanda Mayumi',
        'email': 'mayumi@gmail.com',
        'idade': 22,
        'sexo': 'F',
        'altura': 1.55
    },
    {
        'id': 2,
        'nome': 'Valdir Junior',
        'email': 'junior@gmail.com',
        'idade': 21,
        'sexo': 'M',
        'altura': 1.81
    }
]

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/'+str(version)+'/pessoas', methods=['GET'])
def get_pessoas():
    """
    Só para pegar pessoas.
    Traz todo mundo
    ---
    tags:
      - pessoas
    description: Só para pegar pessoas
    consumes:
      - application/json
    produces:
      - application/json
    responses:
        200:
            description: Deve retornar uma lista de pessoas
            schema:
                $ref: '#/definitions/Pessoa'
    """
    return jsonify({'pessoas': pessoas})

@app.route('/api/'+str(version)+'/pessoas/<int:pessoa_id>', methods=['GET'])
def get_pessoa(pessoa_id):
    """
    Só para pegar quem você quer.
    Traz a pessoa perfeita para você
    ---
    tags:
      - pessoas
    parameters:
      - name: pessoa_id
        in: path
        type: string
        enum: [1, 2, 3]
        required: true
        default: all
        description: Que pessoa você quer?
    description: Só para pegar quem você quer
    consumes:
      - application/json
    produces:
      - application/json
    responses:
        200:
            description: OK
            schema:
                $ref: '#/definitions/Pessoa'
        404:
            description: Not found
    """
    pessoa = [pessoa for pessoa in pessoas if pessoa['id'] == pessoa_id]
    if len(pessoa) == 0:
        abort(404)
    return jsonify({'pessoa': pessoa[0]})

@app.route('/api/'+str(version)+'/pessoas', methods=['POST'])
def create_pessoas():
    """
    Cria a pessoa certa.
    Deixa salvo a pessoa do jeito que você quer
    ---
    tags:
      - pessoas
    parameters:
      - in: "body"
        name: "body"
        description: "A pessoa que você vai criar"
        required: true
        schema:
          $ref: "#/definitions/Pessoa"
    description: Cria a pessoa certa
    consumes:
      - application/json
    produces:
      - application/json
    responses:
        '201':
            description: Deve retornar apenas uma pessoa
            schema:
                $ref: '#/definitions/Pessoa'
        '400':
            description: Bad request
    definitions:
     Pessoa:
        type: "object"
        required:
        - "nome"
        - "email"
        properties:
          nome:
            type: "string"
            example: "Zézinho da Silva"
          email:
            type: "string"
            example: "nome@email.com"
          idade:
            type: "number"
            example: 25
          sexo:
            type: "string"
            example: "M"
          altura:
            type: "number"
            format: "double"
            example: 1.74
    """
    if not request.json or not 'nome' in request.json:
        abort(400)
    if not request.json or not 'email' in request.json:
        abort(400)
    pessoa = {
        'id': pessoas[-1]['id'] + 1,
        'nome': request.json['nome'],
        'email': request.json['email'],
        'idade': request.json['idade'],
        'sexo': request.json['sexo'],
        'altura': request.json['altura']
    }
    pessoas.append(pessoa)
    return jsonify({'pessoa': pessoa}), 201

@app.route('/api/'+str(version)+'/pessoas/<int:pessoa_id>', methods=['PUT'])
def update_pessoa(pessoa_id):
    """
    Deixa a pessoa como você quer.
    Altera as características de uma pessoa que já existe
    ---
    tags:
      - pessoas
    parameters:
      - name: pessoa_id
        in: path
        type: string
        enum: [1, 2, 3]
        required: true
        default: all
        description: Que pessoa você quer?
      - in: "body"
        name: "body"
        description: "As informações que você vai alterar"
        required: true
        schema:
          $ref: "#/definitions/Pessoa"
    description: Deixa a pessoa como você quer
    consumes:
      - application/json
    produces:
      - application/json
    responses:
        204:
            description: OK
        400:
            description: Bad request
        404:
            description: Not found
    """
    pessoa = [pessoa for pessoa in pessoas if pessoa['id'] == pessoa_id]
    if len(pessoa) == 0:
        abort(404)
    if not request.json:
        abort(400)
    pessoa[0]['nome'] = request.json.get('nome', pessoa[0]['nome'])
    pessoa[0]['email'] = request.json.get('email', pessoa[0]['email'])
    pessoa[0]['idade'] = request.json.get('idade', pessoa[0]['idade'])
    pessoa[0]['sexo'] = request.json.get('sexo', pessoa[0]['sexo'])
    pessoa[0]['altura'] = request.json.get('altura', pessoa[0]['altura'])
    return '', 204

@app.route('/api/'+str(version)+'/pessoas/<int:pessoa_id>', methods=['DELETE'])
def delete_pessoa(pessoa_id):
    """
    Some com a pessoa que você quer.
    Deleta determinada pessoa
    ---
    tags:
      - pessoas
    parameters:
      - name: pessoa_id
        in: path
        type: string
        enum: [1, 2, 3]
        required: true
        default: all
        description: Quem vai sumir?
    description: Some com a pessoa que você quer
    consumes:
      - application/json
    produces:
      - application/json
    responses:
        204:
            description: OK
        404:
            description: Not found
    """
    pessoa = [pessoa for pessoa in pessoas if pessoa['id'] == pessoa_id]
    if len(pessoa) == 0:
        abort(404)
    pessoas.remove(pessoa[0])
    return '', 204

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error':'Bad request'}), 400)

if __name__ == '__main__':
    app.run(debug=True)
