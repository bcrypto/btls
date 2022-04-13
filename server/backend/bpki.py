from openssl import openssl
import subprocess
from settings import *
import sys, os, shutil
import signal
import tempfile
import re
import threading
import time
from os.path import expanduser
home = expanduser("~")

def btls_gen_privkey(privfile, curve):
    cmd = 'genpkey -algorithm bign -pkeyopt params:{} -out {}'.format(curve, privfile)
    retcode, block, er__ = openssl(cmd)
    print(retcode, block, er__)
    return retcode

def btls_issue_cert(curve):
    cwd = os.getcwd()
    privfile = os.path.join(cwd, 'priv.key')
    certfile = os.path.join(cwd, 'cert.pem')
    btls_gen_privkey(privfile, curve)
    cmd = ('req -x509 -subj "/CN=www.example.org/O=BCrypto/C=BY/ST=MINSK" -new -key {} -nodes -out {}'
        .format(privfile, certfile))
    retcode, block, er__ = openssl(cmd)
    print(retcode, block, er__)
    retcode, parse, er__ = openssl('asn1parse -in {}'.format(certfile))
    with open(certfile, 'r') as f:
        cert = f.read()
    return cert, parse

def tsa_req(file_, hash='bash256', nonce=True):
    if not nonce:
        cmd = ('ts -query -data {} -{} -out ./out/tsa/req.tsq -no_nonce'.format(file_, hash))
    else:
        cmd = ('ts -query -data {} -{} -out ./out/tsa/req.tsq -cert'.format(file_, hash))
    retcode, block, er__ = openssl(cmd)
    print(file_, hash, nonce, os.getcwd())
    print(er__)
    cmd = ("ts -reply -queryfile ./out/tsa/req.tsq -signer ./out/tsa/cert -passin pass:tsatsatsa -inkey ./out/tsa/privkey -out ./out/tsa/resp.tsr -no_nonce".format())
    retcode, block, er__ = openssl(cmd)
    print(er__)
    return retcode