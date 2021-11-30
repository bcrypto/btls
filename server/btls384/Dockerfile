FROM ubuntu:20.04

RUN apt-get clean 
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
	patch

COPY ./openssl.sh ./
COPY ./nginx.sh ./
COPY ./index.html /etc/nginx/html/index.html
COPY ./priv384.key /etc/nginx/ssl/priv384.key
COPY ./cert384.pem /etc/nginx/ssl/cert384.pem
COPY ./nginx.conf /etc/nginx/nginx.conf
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
