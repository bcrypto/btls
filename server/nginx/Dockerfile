FROM ubuntu:20.04

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install cmake -y -q

RUN apt-get install -y -q \
	wget \
	git \
	python \
	vim \
	nano \
	iptables \
	build-essential \
	php7.4-fpm \
	patch

COPY ./openssl.sh ./
COPY ./nginx.sh ./
COPY ./index.html /etc/nginx/html/index.html
COPY ./check_server.html /etc/nginx/html/check_server.html
RUN mkdir /etc/nginx/ssl_psk_path
COPY ./priv512.key /etc/nginx/ssl/priv512.key
COPY ./cert512.pem /etc/nginx/ssl/cert512.pem
COPY ./priv256.key /etc/nginx/ssl/priv256.key
COPY ./cert256.pem /etc/nginx/ssl/cert256.pem
COPY ./priv384.key /etc/nginx/ssl/priv384.key
COPY ./cert384.pem /etc/nginx/ssl/cert384.pem
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./nginx.patch ./
ENV HOME /root
# WORKDIR $HOME

RUN git clone https://github.com/bcrypto/bee2evp.git
# WORKDIR $HOME/bee2evp/doc
# RUN bash build.sh
RUN bash ./openssl.sh \
WORKDIR '/'
RUN bash ./nginx.sh

WORKDIR $HOME
ENV PREFIX $HOME/bee2evp/build/local
ENV LD_LIBRARY_PATH "${PREFIX}/lib:${LD_LIBRARY_PATH:-}"
ENV PATH ${PREFIX}/bin:${PATH}
EXPOSE 443
EXPOSE 4431
