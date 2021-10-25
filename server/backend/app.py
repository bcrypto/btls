from flask import Flask
from flask import render_template
from flask import request
from openssl import openssl
from test_btls import test_server_btls512, test_server_btls384, test_server_btls256

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
    server_ = request.args.get('test', default = 'nginx', type = str)
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
    ret_codes = test_server_btls512(server_)
    ret_codes += test_server_btls384(server_)
    ret_codes += test_server_btls256(server_)

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
                            ciph5121 = uni_code[0],
                            ciph5122 = uni_code[1],
                            ciph5123 = uni_code[2],
                            ciph5124 = uni_code[3],
                            ciph3841 = uni_code[4],
                            ciph3842 = uni_code[5],
                            ciph3843 = uni_code[6],
                            ciph3844 = uni_code[7],
                            ciph2561 = uni_code[8],
                            ciph2562 = uni_code[9],
                            ciph2563 = uni_code[10],
                            ciph2564 = uni_code[11])

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
