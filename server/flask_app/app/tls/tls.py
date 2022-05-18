from .test_btls import test_server_btls
from flask import request, render_template
from flask import Blueprint

tls_bp = Blueprint('tls_bp', __name__,
                   template_folder='../templates',
                   static_folder='../static')

@tls_bp.route('/')
@tls_bp.route('/tls', methods=['GET'])
def tls():
    data = request.data.decode('utf-8').split('#')
    ciphersuites = ['DHE-BIGN-WITH-BELT-DWP-HBELT', 'DHE-BIGN-WITH-BELT-CTR-MAC-HBELT',
                    'DHT-BIGN-WITH-BELT-DWP-HBELT', 'DHT-BIGN-WITH-BELT-CTR-MAC-HBELT',
                    'DHE-PSK-BIGN-WITH-BELT-DWP-HBELT', 'DHE-PSK-BIGN-WITH-BELT-CTR-MAC-HBELT',
                    'DHT-PSK-BIGN-WITH-BELT-DWP-HBELT', 'DHT-PSK-BIGN-WITH-BELT-CTR-MAC-HBELT']
    ssl_ciphers = []
    for ciph in ciphersuites:
        if ciph in data[1]:
            ssl_ciphers.append(ciph)

    return render_template('tls.html',
                           ssl_cipher=data[0],
                           ssl_curves=data[2],
                           ssl_protocol=data[3],
                           ssl_ciphers=ssl_ciphers,
                           ssl_all=data[1].split(':'))

@tls_bp.route('/tls/check', methods=['GET'])
def check():
    return render_template('check.html')

@tls_bp.route('/tls/check_server', methods=['GET', 'POST'])
def check_server():
    server_ = request.args.get('test', default='btls256', type=str)
    ret_codes = test_server_btls(server_)

    uni_code = []
    for code_ in ret_codes:
        if code_:
            uni_code.append("\u2705")
        else:
            uni_code.append('\u274C')

    return render_template('check_server.html',
                           ciph1=uni_code[0],
                           ciph2=uni_code[1],
                           ciph3=uni_code[2],
                           ciph4=uni_code[3])
