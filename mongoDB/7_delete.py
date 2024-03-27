from pymongo import MongoClient
from bson import ObjectId  # se for tratar de ObjectID

mongodb_uri = "CONNECTION STRING"

client = MongoClient(mongodb_uri)

db = client.get_database("Automotivedb")
collection = db['day1']

# IDs dos documentos a serem deletados:
ids_para_deletar = [
    ObjectId('66032dd4923fca9cb5f58ce9'),
    ObjectId('66032e2866fc6fca4435b4b0'),
    ObjectId('66032e2866fc6fca4435b4b1')
]

# Deletar os documentos na coleção "day1"
for id_documento in ids_para_deletar:
    result = collection.delete_one({"_id": id_documento})
    if result.deleted_count == 1:
        print(f"Documento com ID {id_documento} deletado com sucesso.")
    else:
        print(f"Erro ao deletar o documento com ID {id_documento}.")

client.close()
