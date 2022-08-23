from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

"""
    This program includes crud operation in mongodb through API
"""


client = pymongo.MongoClient("mongodb://sai1118:Sai1234@ac-hfsjren-shard-00-00.d8m7g8f.mongodb.net:27017,ac-hfsjren-shard-00-01.d8m7g8f.mongodb.net:27017,ac-hfsjren-shard-00-02.d8m7g8f.mongodb.net:27017/?ssl=true&replicaSet=atlas-z7p8m3-shard-0&authSource=admin&retryWrites=true&w=majority")
database = client['taskdb']
collection = database['taskcollection']

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        data = {'name' : name, 'number' : number}
        collection.insert_one(data)
    return jsonify(str("inserted successfully"))

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        get_name = str(request.json['get_name'])
        set_number = request.json['set_number']
        collection.update_one({'name': get_name}, {'$set': {'number': set_number}})
    return jsonify(str("updated successfully"))

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        del_name = str(request.json['del_name'])
        collection.delete_one({'name' : del_name})
    return jsonify(str('deleted successfully'))

@app.route('/fetch', methods=['POST'])
def fetch():
    if request.method == 'POST':
        c = collection.find()
        l = []
        for i in c:
            l.append(i)
    return jsonify(str(l))

if __name__ == '__main__':
    app.run(debug=True, port=5002)