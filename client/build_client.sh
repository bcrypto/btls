sudo apt install wget python3 build-essential clang cmake \
ruby pkg-config epiphany-browser meson gnome-pkg-tools \
libglib2.0-dev libproxy-dev \
gsettings-desktop-schemas-dev ca-certificates -y

git clone https://github.com/bcrypto/bee2evp.git
cd bee2evp/test
bash ./build.sh
cd ../..

export PREFIX=${PWD}/bee2evp/build/local
export PKG_CONFIG_PATH=${PREFIX}/lib/pkgconfig:$PKG_CONFIG_PATH
export CPATH=${PREFIX}/include:${CPATH}
export LD_LIBRARY_PATH=${PREFIX}/lib:${LD_LIBRARY_PATH}
export PATH=${PREFIX}/bin:${PATH}
export OPENSSL_CONF=${PREFIX}/openssl.cnf
export GIO_MODULE_DIR=${PREFIX}/lib/x86_64-linux-gnu/gio/modules

echo $PREFIX

git clone --branch 2.64.2 https://gitlab.gnome.org/GNOME/glib-networking.git
cd glib-networking
mkdir build
cd build

which openssl
meson --prefix=${PREFIX} -Dopenssl=enabled -Dgnutls=disabled ..
ninja
ninja install
ln -s /etc/ssl/certs $PREFIX/certs 
