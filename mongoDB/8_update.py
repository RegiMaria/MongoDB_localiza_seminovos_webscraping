from pymongo import MongoClient
from datetime import datetime #datas
from bson import ObjectId    # se for tratar de ObjectID

mongodb_uri = "CONNECTION STRING"
client = MongoClient(mongodb_uri)

db = client.get_database("Automotivedb")
collection = db['day1']



#lógica da alteração aqui




if resultado.modified_count > 0:
    print(" #### corrigidas com sucesso.")
else:
    print("Nenhum documento foi atualizado.")


client.close()

