#!/bin/bash
export OPENSSL_BRANCH=OpenSSL_1_1_1i
export BEE2_BRANCH=master
export PREFIX=/opt/usr/local

cd bee2evp
git submodule update --init --remote
cd ..
git clone --depth 1 -b ${OPENSSL_BRANCH} https://github.com/openssl/openssl.git
cd openssl
git apply ../bee2evp/btls/openssl111i.patch
cp ../bee2evp/btls/btls.c ./ssl/
cp ../bee2evp/btls/btls.h ./ssl/
mkdir build
cd build
../config shared -d --prefix=${PREFIX} --openssldir=${PREFIX}
make -j${nproc}
make install
mv ${PREFIX}/openssl.cnf.dist ${PREFIX}/openssl.cnf
sed -i "/\[ new\_oids\ ]/i openssl_conf = openssl_init\n[ openssl_init ]\nengines = engine_section\n[ engine_section ]\nbee2evp = bee2evp_section\n[ bee2evp_section ]\nengine_id = bee2evp\ndynamic_path = ${PREFIX}/lib/libbee2evp.so\ndefault_algorithms = ALL" ${PREFIX}/openssl.cnf
cd ../../bee2evp/bee2
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_PIC=ON -DCMAKE_INSTALL_PREFIX=${PREFIX} ..
make -j${nproc}
make install
cd ../..
export LD_LIBRARY_PATH="${PREFIX}/lib:${LD_LIBRARY_PATH:-}"
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release \
     -DBEE2_LIBRARY_DIRS=${PREFIX}/lib -DBEE2_INCLUDE_DIRS=${PREFIX}/include \
     -DOPENSSL_LIBRARY_DIRS=${PREFIX}/lib -DOPENSSL_INCLUDE_DIRS=${PREFIX}/include \
     -DLIB_INSTALL_DIR=${PREFIX}/lib -DCMAKE_INSTALL_PREFIX=${PREFIX} ..
make -j${nproc}
make install
echo "export LD_LIBRARY_PATH="${PREFIX}/lib:${LD_LIBRARY_PATH:-}"" >> ${HOME}/.bashrc
echo "export PATH=${PREFIX}/bin:${PATH}" >> ${HOME}/.bashrc
echo ${PREFIX}
echo ${PATH}
echo ${LD_LIBRARY_PATH}
ls ${PREFIX}/lib
ls ${PREFIX}/bin
cp -a ../test/. .