# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import database

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}}, methods=["GET", "POST", "DELETE", "PUT", "OPTIONS"])

# Método para retornar todos os contatos
@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify({'contacts': database.get_all_contacts()}), 200

# Método para adicionar um novo contato
@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.get_json()
    database.add_contact(data)
    return jsonify({'message': 'Contact added successfully', 'contact': data}), 201

# Método para atualizar um contato
@app.route('/contacts/<email>', methods=['PUT'])
def update_contact(email):
    data = request.get_json()
    updated_contact = database.update_contact(email, data)

    if not updated_contact:
        return jsonify({'error': 'Contact not found'}), 404

    return jsonify({'message': 'Contact updated successfully', 'contact': updated_contact}), 200

# Método para excluir um contato específico
@app.route('/contacts/<email>', methods=['DELETE'])
def delete_contact(email):
    deleted_contact = database.delete_contact(email)
    if not deleted_contact:
        return jsonify({'error': 'Contact not found'}), 404
    return jsonify({'message': 'Contact deleted successfully'}), 200