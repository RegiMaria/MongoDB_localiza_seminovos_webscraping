from pymongo import MongoClient

mongodb_uri = "CONNECTION STRING"

client = MongoClient(mongodb_uri)

# Acessa banco de dados "Automotivedb"
db = client.get_database("Automotivedb")

# Exibir as coleções:
print(db.list_collection_names())

# Fechar a conexão:
client.close()