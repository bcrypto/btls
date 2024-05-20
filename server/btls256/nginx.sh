wget https://sourceforge.net/projects/pcre/files/pcre/8.45/pcre-8.45.tar.gz
tar -zxf pcre-8.45.tar.gz
cd pcre-8.45
./configure
make
make install
cd ..

wget http://zlib.net/zlib-1.3.1.tar.gz
tar -zxf zlib-1.3.1.tar.gz
ls /
cd zlib-1.3.1
./configure
make
make install
cd ..

wget https://nginx.org/download/nginx-1.18.0.tar.gz
tar -zxf nginx-1.18.0.tar.gz
#cp ./nginx.patch ./nginx-1.21.3/nginx.patch
cd nginx-1.18.0
#patch -p1 -i nginx.patch
ls /
./configure --pid-path=/usr/local/nginx/nginx.pid --with-pcre=/pcre-8.45 --with-zlib=/zlib-1.3.1 --with-http_ssl_module --with-stream --prefix=/etc/nginx --sbin-path=/usr/sbin/nginx --conf-path=/etc/nginx/nginx.conf --with-ld-opt="-L /opt/usr/local/lib" --with-cc-opt="-I /opt/usr/local/include"
make
make install
cd ..