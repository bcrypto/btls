# Btls: The Transport Layer Security Protocol

![](figs/btls-logo-small.png)

[![build](https://github.com/bcrypto/btls/actions/workflows/build.yaml/badge.svg)](https://github.com/bcrypto/btls/actions/workflows/build.yaml)

## What is Btls?

Btls is the informal name of STB 34.101.65, the official standard of Belarus.
Btls compiles several RFC that defines the 
[Transport Layer Security (TLS)](https://en.wikipedia.org/wiki/Transport_Layer_Security) 
protocol and its extensions legalizing 
[TLS 1.2](https://www.rfc-editor.org/rfc/rfc5246.txt) in Belarus.

Btls also defines 8 ciphersuites based on algorithms of 
[STB 34.101.31](https://github.com/bcrypto/belt) 
and [STB 34.101.45](https://github.com/bcrypto/bign).

## Reference implementation

Ciphersuites of Btls are implemented [here](https://github.com/bcrypto/bee2evp) 
via a patch for [OpenSSL](https://github.com/openssl/openssl). 

## What is this repo?

In this repo, we process comments on the current version of Btls,
discuss future versions, provide additional supporting material.

The latest releases of Btls can be found at 
[Releases](https://github.com/bcrypto/btls/releases).

Comments and proposals are processed at 
[Issues](https://github.com/bcrypto/btls/issues). 

## Set up client

![Client](/figs/client.png)

### Building

```console
$ cd client
$ bash build_cliens.sh
$ cd ..
```

After building:
```console
$ export PREFIX=${PWD}/bee2evp/build/local
$ echo "export LD_LIBRARY_PATH=${PREFIX}/lib:$LD_LIBRARY_PATH" >> ${HOME}/.bashrc
$ echo "export PATH=${PREFIX}/bin:$PATH" >> ${HOME}/.bashrc
$ echo "export PKG_CONFIG_PATH=${PREFIX}/lib/pkgconfig" >> ${HOME}/.bashrc
$ echo "export CPATH=${PREFIX}/include:$CPATH" >> ${HOME}/.bashrc
$ echo "export OPENSSL_CONF=${PREFIX}/openssl.cnf" >> ${HOME}/.bashrc
$ echo "export GIO_MODULE_DIR=${PREFIX}/lib/x86_64-linux-gnu/gio/modules" >> ${HOME}/.bashrc
```
or run sh script:
```console
$ bash ./add_to_bashrc.sh
```

### Using

```console
$ epiphany https://<server>
\\ if server is local <server>=127.0.0.1
```
Enter server ip in the text area and press button "Test".

## Set up server

![Client](/figs/server.png)

Requirements:

1. [docker](https://docs.docker.com/engine/install/ubuntu/)
2. [docker-compose](https://docs.docker.com/compose/install/)

```console
$ sudo docker pull btls/nginx-btls
$ sudo docker pull btls/flask
$ sudo docker-compose up -d --force
```

Open 2 terminals.

In the first:
```console
$ sudo docker exec -it nginx-btls bash
// in the docker shell
$ nginx -g "daemon off;" 
```
In the second:
```console
$ sudo docker exec -it flask bash
// in the docker shell
$ flask run --host=0.0.0.0 --port=5000
```