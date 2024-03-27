from pymongo import MongoClient

mongodb_uri = "CONNECTION STRING"

client = MongoClient(mongodb_uri)

# Acessar o banco de dados "Automotivedb"
db = client.get_database("Automotivedb")

collection = db['day1']
# Consulta para buscar TODOS os documentos na coleção "day1"
documentos = collection.find()

# Iterar sobre os documentos e retorna seus valores:
for documento in documentos:
    print(documento)

    # Fechar a conexão com o MongoDB
    client.close()