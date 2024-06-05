export PREFIX=${PWD}/bee2evp/build/local
export PKG_CONFIG_PATH=${PREFIX}/lib/pkgconfig:$PKG_CONFIG_PATH
export CPATH=${PREFIX}/include:${CPATH}
export LD_LIBRARY_PATH=${PREFIX}/lib:${LD_LIBRARY_PATH}
export PATH=${PREFIX}/bin:${PATH}
export OPENSSL_CONF=${PREFIX}/openssl.cnf
export GIO_MODULE_DIR=${PREFIX}/lib/x86_64-linux-gnu/gio/modules

epiphany