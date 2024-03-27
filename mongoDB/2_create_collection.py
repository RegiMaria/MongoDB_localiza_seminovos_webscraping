from pymongo import MongoClient

mongodb_uri = "CONNECTION STRING"
client = MongoClient(mongodb_uri)

db = client.get_database("Automotivedb")

# Cria nova coleção chamada "day1"
db.create_collection("day1")

# Verificando se a coleção foi criada:

if "day1" in db.list_collection_names():
    print("A coleção 'day1' foi criada com sucesso!")
else:
    print("Erro ao criar a coleção 'day1'.")

# Fechando a conexão com o MongoDB
client.close()