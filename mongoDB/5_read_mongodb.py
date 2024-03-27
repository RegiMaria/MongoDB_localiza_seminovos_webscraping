from pymongo import MongoClient

mongodb_uri = "CONNECTION STRING"

client = MongoClient(mongodb_uri)

# Acessar o banco de dados "Automotivedb"
db = client.get_database("Automotivedb")

client.close()

