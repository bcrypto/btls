# *****************************************************************************
# \file test.py
# \project bee2evp [EVP-interfaces over bee2 / engine of OpenSSL]
# \brief Python tests for openssl[bee2evp]
# \created 2019.07.10
# \version 2021.03.18
# \license This program is released under the GNU General Public License 
# version 3 with the additional exemption that compiling, linking, 
# and/or using OpenSSL is allowed. See Copyright Notices in bee2evp/info.h.
# *****************************************************************************

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

def test_server_btls256(server_):
	ans = ''
	print("s_client -connect {} -curves bign-curve256v1 -cipher DHE-BIGN-WITH-BELT-CTR-MAC-HBELT -tls1_2".format(server_))
	ret_code1, out, err__ = openssl("s_client -connect {} -curves bign-curve256v1 -cipher DHE-BIGN-WITH-BELT-CTR-MAC-HBELT -tls1_2".format(server_), prefix='echo testBTLS |'"")  #, prefix='echo testBTLS |'"", type_=0)
	ans += out.decode('utf-8')
	ret_code2, out, err__ = openssl("s_client -connect {} -curves bign-curve256v1 -cipher DHE-BIGN-WITH-BELT-DWP-HBELT -tls1_2".format(server_), prefix='echo testBTLS |'"")  #, prefix='echo testBTLS |'"", type_=0)
	ans += out.decode('utf-8')
	ret_code3, out, err__ = openssl("s_client -connect {} -curves bign-curve256v1 -cipher DHT-BIGN-WITH-BELT-CTR-MAC-HBELT -tls1_2".format(server_), prefix='echo testBTLS |'"")  #, prefix='echo testBTLS |'"", type_=0)
	ans += out.decode('utf-8')
	ret_code4, out, err__ = openssl("s_client -connect {} -curves bign-curve256v1 -cipher DHT-BIGN-WITH-BELT-DWP-HBELT -tls1_2".format(server_), prefix='echo testBTLS |'"")  #, prefix='echo testBTLS |'"", type_=0)
	ans += out.decode('utf-8')
	print(server_, err__)
	# result = ret_code1 & ret_code2 & ret_code3 & ret_code4
	return ret_code1, ret_code2, ret_code3, ret_code4

def test_server_btls384(server_):
	ans = ''
	ret_code1, out, err__ = openssl("s_client -connect {} -curves bign-curve384v1 -cipher DHE-BIGN-WITH-BELT-CTR-MAC-HBELT -tls1_2".format(server_), prefix='echo testBTLS |'"")  #, prefix='echo testBTLS |'"", type_=0)
	ans += out.decode('utf-8')
	ret_code2, out, err__ = openssl("s_client -connect {} -curves bign-curve384v1 -cipher DHE-BIGN-WITH-BELT-DWP-HBELT -tls1_2".format(server_), prefix='echo testBTLS |'"")  #, prefix='echo testBTLS |'"", type_=0)
	ans += out.decode('utf-8')
	ret_code3, out, err__ = openssl("s_client -connect {} -curves bign-curve384v1 -cipher DHT-BIGN-WITH-BELT-CTR-MAC-HBELT -tls1_2".format(server_), prefix='echo testBTLS |'"")  #, prefix='echo testBTLS |'"", type_=0)
	ans += out.decode('utf-8')
	ret_code4, out, err__ = openssl("s_client -connect {} -curves bign-curve384v1 -cipher DHT-BIGN-WITH-BELT-DWP-HBELT -tls1_2".format(server_), prefix='echo testBTLS |'"")  #, prefix='echo testBTLS |'"", type_=0)
	ans += out.decode('utf-8')
	print(err__)
	# result = ret_code1 & ret_code2 & ret_code3 & ret_code4
	return ret_code1, ret_code2, ret_code3, ret_code4

def test_server_btls512(server_):
	ans = ''
	ret_code1, out, err__ = openssl("s_client -connect {} -curves bign-curve512v1 -cipher DHE-BIGN-WITH-BELT-CTR-MAC-HBELT -tls1_2".format(server_), prefix='echo testBTLS |'"")  #, prefix='echo testBTLS |'"", type_=0)
	ans += out.decode('utf-8')
	ret_code2, out, err__ = openssl("s_client -connect {} -curves bign-curve512v1 -cipher DHE-BIGN-WITH-BELT-DWP-HBELT -tls1_2".format(server_), prefix='echo testBTLS |'"")  #, prefix='echo testBTLS |'"", type_=0)
	ans += out.decode('utf-8')
	ret_code3, out, err__ = openssl("s_client -connect {} -curves bign-curve512v1 -cipher DHT-BIGN-WITH-BELT-CTR-MAC-HBELT -tls1_2".format(server_),prefix='echo testBTLS |'"")  #, prefix='echo testBTLS |'"", type_=0)
	ans += out.decode('utf-8')
	ret_code4, out, err__ = openssl("s_client -connect {} -curves bign-curve512v1 -cipher DHT-BIGN-WITH-BELT-DWP-HBELT -tls1_2".format(server_), prefix='echo testBTLS |'"")  #, prefix='echo testBTLS |'"", type_=0)
	ans += out.decode('utf-8')
	print(err__)
	# result = ret_code1 & ret_code2 & ret_code3 & ret_code4
	return ret_code1, ret_code2, ret_code3, ret_code4


def btls_gen_privkey(privfile, curve):
	cmd = 'genpkey -algorithm bign -pkeyopt params:{} -out {}'.format(curve, privfile)
	retcode, block, er__ = openssl(cmd)

def btls_issue_cert(privfile, certfile):
	cmd = ('req -x509 -subj "/CN=www.example.org/O=BCrypto/C=BY/ST=MINSK" -new -key {} -nodes -out {}'
		.format(privfile, certfile))
	retcode, block, er__ = openssl(cmd)
