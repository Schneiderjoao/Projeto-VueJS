# database.py

from pymongo import MongoClient

# Conectando ao MongoDB local
client = MongoClient('mongodb://localhost:27017/')
db = client['bancoContatos']  # Nome do banco
contacts_collection = db['contatos']  # Nome da coleção (tipo uma tabela)

def get_all_contacts():
    return list(contacts_collection.find({}, {'_id': 0}))  # Retira o _id do retorno

def get_contact_by_email(email):
    return contacts_collection.find_one({'email': email}, {'_id': 0})

def add_contact(contact):
    contacts_collection.insert_one(contact)

def update_contact(email, data):
    result = contacts_collection.update_one({'email': email}, {'$set': data})
    if result.matched_count:
        return get_contact_by_email(email)
    return None

def delete_contact(email):
    result = contacts_collection.delete_one({'email': email})
    return result.deleted_count > 0