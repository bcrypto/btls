FROM python:3.9

RUN apt-get update
RUN apt-get install -y -q \
    wget \
    git \
    nano \
    build-essential

RUN DEBIAN_FRONTEND=noninteractive apt-get install cmake -y -q

COPY ./requirements.txt /
RUN pip3 install -r requirements.txt
COPY ./openssl.sh /
RUN bash openssl.sh

WORKDIR /
EXPOSE 5000
