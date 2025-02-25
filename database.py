from flask import Flask,jsonify,request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://johansyahmichael:roGB0mAiA7KLf4L0@cluster0.z2wc6.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['MyDatabase'] # ganti sesuai dengan nama database kalian
my_collections = db['MyCollection'] # ganti sesuai dengan nama collections kalian

# Data yang ingin dimasukkan
murid_1 = {'nama':'John Doe','Jurusan':'IPS','Nilai':90}
murid_2 = {'nama':'Jane Doe', 'Jurusan':'IPA','Nilai':85}

results = my_collections.insert_many([murid_1,murid_2])
print(results.inserted_ids) # akan menghasilkan ID dari data yang kita masukkan

for x in my_collections.find():
    print(x)