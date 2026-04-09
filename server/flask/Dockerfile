FROM python:3.12

RUN pip install flask
RUN apt-get update

RUN apt-get install -y -q \
	wget \
	git \
	python3 \
	vim \
	nano \
	iptables \
	build-essential \
	cmake

ENV HOME /root
WORKDIR $HOME

RUN git clone https://github.com/bcrypto/bee2evp.git
WORKDIR $HOME/bee2evp
RUN ls -lah /
RUN BEE2EVP_INSTALL_DIR=/opt/usr/local bash scripts/build.sh -s -b -t openssl-3.5.5

ENV PREFIX $HOME/bee2evp/build/local
ENV LD_LIBRARY_PATH "${PREFIX}/lib:${LD_LIBRARY_PATH:-}"
ENV PATH ${PREFIX}/bin:${PATH}

EXPOSE 5000
