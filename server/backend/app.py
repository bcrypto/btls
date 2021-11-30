from flask import Flask
from flask import render_template
from flask import request
from openssl import openssl
from test_btls import test_server_btls

app = Flask(__name__)

'''@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        server = request.form['test_btls']
        test_btls()
        #return "<h1>Hello, World!<h1>"
        return render_template('index.html')'''

#@app.route('/')
#def index():
#    return render_template('index.html')
    #return "<h1>Hello from BTLS<h1>"

@app.route('/check_server', methods=['GET', 'POST'])
def check_server():
    server_ = request.args.get('test', default = 'btls256', type = str)
    print(server_)
    data = request.data.decode('utf-8').split('#')
    ssl_cipher = data[0]
    ciphersuites = ['DHE-BIGN-WITH-BELT-DWP-HBELT', 'DHE-BIGN-WITH-BELT-CTR-MAC-HBELT',
                     'DHT-BIGN-WITH-BELT-DWP-HBELT', 'DHT-BIGN-WITH-BELT-CTR-MAC-HBELT',
                     'DHE-PSK-BIGN-WITH-BELT-DWP-HBELT', 'DHE-PSK-BIGN-WITH-BELT-CTR-MAC-HBELT',
                     'DHT-PSK-BIGN-WITH-BELT-DWP-HBELT', 'DHT-PSK-BIGN-WITH-BELT-CTR-MAC-HBELT']
    ssl_ciphers = []
    for ciph in ciphersuites:
        if ciph in data[1]:
            ssl_ciphers.append(ciph)
    # ssl_ciphers = ':'.join(ssl_ciphers)
    print(ssl_cipher)
    print(ssl_ciphers)
    ssl_curves = data[2]
    print(ssl_curves)
    ssl_protocol = data[3]
    print(ssl_protocol)
    ret_codes = test_server_btls(server_)

    uni_code =[]
    for code_ in ret_codes:
        if code_:
            uni_code.append("\u2705")
        else:
            uni_code.append('\u274C')

    return render_template('check_server.html',
                            ssl_cipher=data[0],
                            ssl_ciphers=ssl_ciphers,
                            ssl_curves=data[2],
                            ssl_protocol=data[3],
                            ssl_all=data[1],
                            ciph1 = uni_code[0],
                            ciph2 = uni_code[1],
                            ciph3 = uni_code[2],
                            ciph4 = uni_code[3])

#@app.route('/check_client', methods=['GET', 'POST'])
#def check_client():
#    #if request.method == 'GET':
#    #server = request.form['test_btls']
#    ans = ''
#    data = request.data.decode('utf-8').split('#')
#    host = data[0]
#    curve = data[1]
#    print(data)
#    print(host)
#    if (curve == 'bign-curve256v1'):
#        ans = test_client_btls256(host)
#        return ans
    #return ans
    #return "<h1>Hello, World!<h1><h2>" + str(data) + "<h2>"
    #if request.method == 'GET':
    #    ciphersuite = request.form['ciphersuite']


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
