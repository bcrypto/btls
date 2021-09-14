FROM ubuntu:20.04

RUN echo $HOME

RUN apt-get update

RUN apt-get install -y -q \
	git \
	python \
	vim \
	nano iptables \
	build-essential \
	wget

RUN DEBIAN_FRONTEND=noninteractive apt-get install cmake -y

RUN git clone https://github.com/bcrypto/bee2evp.git

COPY ./server/openssl.sh ./
COPY ./server/nginx.sh ./
COPY ./server/index.html /etc/nginx/html/index.html
COPY ./server/btls512.key /etc/nginx/ssl/btls512.key
COPY ./server/cert512.pem /etc/nginx/ssl/cert512.pem
COPY ./server/nginx.conf /etc/nginx/nginx.conf

RUN bash ./openssl.sh
WORKDIR "/"
RUN bash ./nginx.sh
RUN ldconfig

ENV HOME /root
WORKDIR $HOME

ENV PREFIX /opt/usr/local
ENV LD_LIBRARY_PATH "${PREFIX}/lib:${LD_LIBRARY_PATH:-}"
ENV PATH ${PREFIX}/bin:${PATH}
EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]
