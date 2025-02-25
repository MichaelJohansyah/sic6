from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)

# Koneksi ke MongoDB Atlas
uri = "mongodb+srv://johansyahmichael:roGB0mAiA7KLf4L0@cluster0.z2wc6.mongodb.net/?appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["sensor_database"]
collection = db["data_sensor"]

@app.route('/sensor', methods=['POST'])
def receive_sensor_data():
    data = request.json
    if not data:
        return jsonify({"error": "No data received"}), 400

    # Simpan ke MongoDB
    collection.insert_one(data)

    return jsonify({"message": "Data stored successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)