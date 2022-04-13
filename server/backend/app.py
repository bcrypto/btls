from openssl import openssl
from test_btls import test_server_btls
from bpki import btls_issue_cert, tsa_req
import os
from flask import Flask, request, jsonify, render_template, send_file
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

mongo = PyMongo(app)
db = mongo.db

@app.route('/todo')
def todo():
    _todos = db.todo.find()

    item = {}
    data = []
    for todo in _todos:
        item = {
            'id': str(todo['_id']),
            'todo': todo['todo']
        }
        data.append(item)

    return jsonify(
        status=True,
        data=data
    )

@app.route('/todo', methods=['POST'])
def createTodo():
    data = request.get_json(force=True)
    item = {
        'todo': data['todo']
    }
    db.todo.insert_one(item)

    return jsonify(
        status=True,
        message='To-do saved successfully!'
    ), 201

@app.route('/issue_cert', methods=['GET'])
def genCert():
    curve = request.args.get('curve', default='bign-curve256v1', type=str)
    cert, parse = btls_issue_cert(curve)
    return jsonify(
        cert = cert,
        parse = parse
    ), 201

@app.route('/tsa', methods=['GET', 'POST'])
def reqTS():
    data = request.data.decode('utf-8').split('#')
    file_ = data[1] # request.args.get('file', default='tsa.sh', type=str)
    hash_ = data[0] # request.args.get('hash', default='bash256', type=str)
    nonce_ = data[2] # request.args.get('nonce', default='False', type=str)
    tsa_req(file_, hash_, nonce_ == 'True')
    return send_file('./out/tsa/resp.tsr')


'''@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        server = request.form['test_btls']
        test_btls()
        #return "<h1>Hello, World!<h1>"
        return render_template('index.html')'''

@app.route('/', methods=['GET', 'POST'])
def index():
    data = request.data.decode('utf-8').split('#')
    ciphersuites = ['DHE-BIGN-WITH-BELT-DWP-HBELT', 'DHE-BIGN-WITH-BELT-CTR-MAC-HBELT',
                     'DHT-BIGN-WITH-BELT-DWP-HBELT', 'DHT-BIGN-WITH-BELT-CTR-MAC-HBELT',
                     'DHE-PSK-BIGN-WITH-BELT-DWP-HBELT', 'DHE-PSK-BIGN-WITH-BELT-CTR-MAC-HBELT',
                     'DHT-PSK-BIGN-WITH-BELT-DWP-HBELT', 'DHT-PSK-BIGN-WITH-BELT-CTR-MAC-HBELT']
    ssl_ciphers = []
    for ciph in ciphersuites:
        if ciph in data[1]:
            ssl_ciphers.append(ciph)

    return render_template('index.html',
                            ssl_cipher=data[0],
                            ssl_curves=data[2],
                            ssl_protocol=data[3],
                            ssl_ciphers = ssl_ciphers,
                            ssl_all=data[1].split(':'))
    #return "<h1>Hello from BTLS<h1>"

@app.route('/check_server', methods=['GET', 'POST'])
def check_server():
    server_ = request.args.get('test', default = 'btls256', type = str)
    ret_codes = test_server_btls(server_)

    uni_code =[]
    for code_ in ret_codes:
        if code_:
            uni_code.append("\u2705")
        else:
            uni_code.append('\u274C')

    return render_template('check_server.html',
                            ciph1 = uni_code[0],
                            ciph2 = uni_code[1],
                            ciph3 = uni_code[2],
                            ciph4 = uni_code[3])


if __name__ == '__main__':
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
