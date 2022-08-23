from flask import Flask, request, jsonify
import mysql.connector as conn

app = Flask(__name__)

@app.route('/testfun')
def test():
    get_name = request.args.get('get_name')
    mobile_number = request.args.get('mobile')
    mail_id = request.args.get('mail')
    return "This is my first function for get {} {} {}".format(get_name, mobile_number, mail_id)

@app.route('/get_data',)
def get_data_from():
    db = request.args.get('db')
    tn = request.args.get('tn')
    try:
        connection = conn.connect(host='localhost', user='root', passwd='Root_mysql', database=db)
        cursor = connection.cursor()
        cursor.execute('select * from tasktable')
        data = cursor.fetchall()
        connection.commit()
        connection.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5002)