from flask import Blueprint, render_template
from flask import request, send_file
from .test_bpki import tsa_req

bpki_bp = Blueprint('bpki_bp', __name__,
                    template_folder='../templates',
                    static_folder='../static')


@bpki_bp.route('/bpki', methods=['GET'])
def bpki():
    return render_template('bpki.html')

@bpki_bp.route('/bpki/req_ts', methods=['GET'])
def req_ts():
    file_ = request.args.get('file', type=str).strip()
    hash_ = request.args.get('hash', type=str).strip()
    nonce_ = request.args.get('nonce', type=str).strip()
    tsa_req(file_, hash_, nonce_ == 'True')
    return send_file('/flask_app/out/tsa/resp.tsr')
