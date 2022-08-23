from flask import Flask, request, jsonify
import mysql.connector as conn

app = Flask(__name__)

connection = conn.connect(host='localhost', user='root', passwd='Root_mysql')
cursor = connection.cursor()
cursor.execute('create database if not exists tasksql')
cursor.execute('create table if not exists tasksql.tasktable(name varchar(30), number int)')

"""
    This program includes CRUD operation in mysql through API
"""

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into tasksql.tasktable values(%s, %s)", (name, number))
        # cursor.execute(f"insert into tasksql.tasktable values(%s, %s),{name}, {number}")
        connection.commit()
        return jsonify(str('successfully inserted'))


@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        get_name = request.json['get_name']
        print(get_name)
        cursor.execute('update tasksql.tasktable set number = number + 500 where name = %s', (get_name,))
        #cursor.execute(f'update tasksql.tasktable set number = number + 500 where name = "{get_name}"')
        connection.commit()
        return jsonify(str('updated successfully'))

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        name_del = request.json['name_del']
        cursor.execute(f'delete from tasksql.tasktable where name = "{name_del}"')
        #cursor.execute('delete from tasksql.tasktable where name = %s', (name_del,))
        connection.commit()
        return jsonify(str('deleted successfully'))

@app.route('/fetch', methods=['POST'])
def fetch_data():
    if request.method == 'POST':
        cursor.execute('select * from tasksql.tasktable')
        l = []
        for i in cursor.fetchall():
            l.append(i)
        return jsonify(str(l))

if __name__ == '__main__':
    app.run(debug=True, port=5002)
