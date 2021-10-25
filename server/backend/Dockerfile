FROM python:3.9

#RUN apt-get update
RUN pip install flask
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install cmake -y -q

RUN apt-get install -y -q \
	wget \
	git \
	python \
	vim \
	nano \
	iptables \
	build-essential

COPY ./openssl.sh ./
ENV HOME /root
# WORKDIR $HOME

RUN git clone https://github.com/bcrypto/bee2evp.git
# WORKDIR $HOME/bee2evp/doc
# RUN bash build.sh
RUN bash ./openssl.sh
ENV PREFIX $HOME/bee2evp/build/local
ENV LD_LIBRARY_PATH "${PREFIX}/lib:${LD_LIBRARY_PATH:-}"
ENV PATH ${PREFIX}/bin:${PATH}
#RUN apt-get install echo -y -q
#WORKDIR /backend

#COPY requirements.txt /backend
#RUN pip3 install --upgrade pip -r requirements.txt
#RUN apt-get install vim -y -q

#COPY . /backend

EXPOSE 5000
#EXPOSE 443
#ENTRYPOINT [ "python3", "app.py" ]