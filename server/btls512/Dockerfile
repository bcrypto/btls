FROM ubuntu:24.04

RUN apt-get clean 
RUN apt-get update

RUN apt-get install -y -q \
	wget \
	git \
	python3 \
	vim \
	nano \
	iptables \
	build-essential \
	patch \
	cmake

COPY ./nginx.sh ./
COPY ./index.html /etc/nginx/html/index.html
COPY ./priv512.key /etc/nginx/ssl/priv512.key
COPY ./cert512.pem /etc/nginx/ssl/cert512.pem
COPY ./nginx.conf /etc/nginx/nginx.conf
ENV HOME /root
WORKDIR $HOME

RUN git clone https://github.com/bcrypto/bee2evp.git
WORKDIR $HOME/bee2evp
RUN BEE2EVP_INSTALL_DIR=/opt/usr/local bash scripts/build.sh -s -b -t openssl-3.3.1

WORKDIR '/'
RUN bash ./nginx.sh

WORKDIR $HOME
ENV PREFIX /opt/usr/local
ENV LD_LIBRARY_PATH "${PREFIX}/lib:${LD_LIBRARY_PATH:-}"
ENV PATH ${PREFIX}/bin:${PATH}
EXPOSE 443
EXPOSE 8443
EXPOSE 8444
EXPOSE 8445
EXPOSE 8446
