# MongoDB shell Scripts "Mongosh"

# CREATE DB:
 use <name your db>

#CREATE COLLECTION:

db.createCollection("yourcollection's name")

#CREATE A DOC IN COLLECTION:

db. yourcollection.insertOne ({'first data your collection'})

#READ ALL DOC -RETURN ALL ITEMS:

db.yourcollection.find ({})

#READ ONE ITEM'S DOC:
db. yourcollection.findOne({"exemple": "exemple"})

#UPDATE:
db.yourcollection.updateOne (
    {"marca": "FIAT"},
    {$set : {"marca": "RENAULT"}}
)

#COUNT DOC IN COLLECTION:
db.yourcollection.countDocuments({})

#DELETE COLLECTION:
db.yourcollection.drop({})

#DELETE ITEMS COLLECTION:
db.yourcollection.deletemany({})

