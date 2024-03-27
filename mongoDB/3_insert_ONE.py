from pymongo import MongoClient

mongodb_uri = "CONNECTION STRING"

client = MongoClient(mongodb_uri)

db = client.get_database("Automotivedb")

collection = db['day1']

documento = {
    "data": 26/2/2024,
    "marca": "FIAT",
    "modelo": "MOBI LIKE 1.0",
    "ano": 2022,
    "km": 76.576,
    "preco": 49.990
}
# Inserir o documento na coleção "day1":
result = collection.insert_one(documento)

# Verificar se a inserção foi bem-sucedida
if result.inserted_id:
    print("Documento inserido com sucesso na coleção day1!")
else:
    print("Erro ao inserir o documento.")



client.close()