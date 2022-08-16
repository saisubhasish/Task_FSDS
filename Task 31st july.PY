import pymongo
import json
import logging


"""
    This is my code to read data in mongodb
"""
logging.basicConfig(filename='Task.log', level=logging.INFO)

client = pymongo.MongoClient("mongodb://sai1118:Sai1234@ac-hfsjren-shard-00-00.d8m7g8f.mongodb.net:27017,ac-hfsjren-shard-00-01.d8m7g8f.mongodb.net:27017,ac-hfsjren-shard-00-02.d8m7g8f.mongodb.net:27017/?ssl=true&replicaSet=atlas-z7p8m3-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

try:
    database = client['fitbit']
    conn = database['fitBitTable']
    with open("D:/FSDS-iNeuron/3.Resource/31st July live class Pandas/FitBit_dataset.json") as file:
        file_data = json.load(file)

    for i in file_data:
        print(i)

    if isinstance(file_data, list):
        conn.insert_many(file_data)
    else:
        conn.insert_one(file_data)

    for i in conn.find():
        print(i)

    for i in conn.find():
        logging.info(i)

except Exception as e:
    logging.exception(e)

