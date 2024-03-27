from pymongo import MongoClient

mongodb_uri = "CONNECTION STRING"

client = MongoClient(mongodb_uri)

db = client.get_database("Automotivedb")

collection = db['day1']

dados = [
    {
    "data": 26/2/2024,
    "marca": "HYUNDAI",
    "modelo": "HB20 SENSE 1.0",
    "ano": 2022,
    "km": 58.682,
    "preco": 62.290
},
    {
    "data": 26/2/2024,
    "marca": "FIAT",
    "modelo": "MOBI LIKE 1.0",
    "ano": 2022,
    "km": 52.762,
    "preco": 54.790

    },
    {
    "data": 26/2/2024,
    "marca": "FIAT",
    "modelo": "COROLLA ALTIS HYBRID AT 1.8 4P",
    "ano": 2022,
    "km": 25.918,
    "preco": 155.190
    }

]

# Inseri o documento na coleção "day1"
result = collection.insert_many(dados)

# Verificar se a inserção foi bem-sucedida
if result.inserted_ids:
    print("dados inseridos com sucesso na coleção 'day1' database Automotivedb!")
else:
    print("Erro ao inserir os dados.")

client.close()