from app.openssl import openssl
from os.path import expanduser

home = expanduser("~")


def test_server_btls(server_):
    ans = ''
    print("s_client -connect {} -cipher DHE-BIGN-WITH-BELT-CTR-MAC-HBELT -tls1_2".format(server_))
    ret_code1, out, err__ = openssl(
        "s_client -connect {} -cipher DHE-BIGN-WITH-BELT-CTR-MAC-HBELT -tls1_2".format(server_),
        prefix='echo testBTLS |', type_=0)
    ans += out.decode('utf-8')
    ret_code2, out, err__ = openssl("s_client -connect {} -cipher DHE-BIGN-WITH-BELT-DWP-HBELT -tls1_2".format(server_),
                                    prefix='echo testBTLS |', type_=0)
    ans += out.decode('utf-8')
    ret_code3, out, err__ = openssl(
        "s_client -connect {} -cipher DHT-BIGN-WITH-BELT-CTR-MAC-HBELT -tls1_2".format(server_),
        prefix='echo testBTLS |', type_=0)
    ans += out.decode('utf-8')
    ret_code4, out, err__ = openssl("s_client -connect {} -cipher DHT-BIGN-WITH-BELT-DWP-HBELT -tls1_2".format(server_),
                                    prefix='echo testBTLS |', type_=0)
    ans += out.decode('utf-8')
    return ret_code1, ret_code2, ret_code3, ret_code4
