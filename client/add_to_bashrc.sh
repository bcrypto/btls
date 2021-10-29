export PREFIX=${PWD}/bee2evp/build/local
echo "export LD_LIBRARY_PATH=${PREFIX}/lib:\$LD_LIBRARY_PATH" >> ${HOME}/.bashrc
echo "export PATH=${PREFIX}/bin:\$PATH" >> ${HOME}/.bashrc
echo "export PKG_CONFIG_PATH=${PREFIX}/lib/pkgconfig" >> ${HOME}/.bashrc
echo "export CPATH=${PREFIX}/include:\$CPATH" >> ${HOME}/.bashrc
echo "export OPENSSL_CONF=${PREFIX}/openssl.cnf" >> ${HOME}/.bashrc
echo "export GIO_MODULE_DIR=${PREFIX}/lib/x86_64-linux-gnu/gio/modules" >> ${HOME}/.bashrc
source ~/.bashrc