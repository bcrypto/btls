#FROM python:3.9
FROM python:3.6.8

ENV GROUP_ID=1000 USER_ID=1000

RUN addgroup --gid $GROUP_ID www
RUN adduser --uid $USER_ID --gid $GROUP_ID --disabled-password www
RUN passwd -d www
USER www

RUN apt-get update
RUN apt-get install -y -q \
    wget \
    git \
    nano \
    build-essential \
    sudo

RUN DEBIAN_FRONTEND=noninteractive apt-get install cmake -y -q

# RUN bash tsa.sh

LABEL MAINTAINER="Yahor Laurenau lawre18@gmail.com"

WORKDIR '/home/www'

ADD ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
ADD . /home/www/
RUN pip install gunicorn flask-bootstrap


#ENV HOME /root

COPY ./openssl.sh ./
COPY ./ ./
RUN git clone https://github.com/bcrypto/bee2evp.git
# WORKDIR $HOME/bee2evp/doc
# RUN bash build.sh
RUN pwd
RUN bash ./openssl.sh
ENV PREFIX /opt/usr/local
ENV LD_LIBRARY_PATH "${PREFIX}/lib:${LD_LIBRARY_PATH:-}"
ENV PATH ${PREFIX}/bin:${PATH}
# ENV HOME /home/www/

RUN bash setup.sh
#USER www
EXPOSE 5000

#ENTRYPOINT [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]

#RUN apt-get update
#RUN pip install flask gunicorn
#RUN apt-get update
#RUN DEBIAN_FRONTEND=noninteractive apt-get install cmake -y -q

#RUN apt-get install -y -q \
#   wget \
#   git \
#   python \
#   vim \
#   nano \
#   iptables \
#   build-essential


# WORKDIR $HOME

#RUN git clone https://github.com/bcrypto/bee2evp.git
# WORKDIR $HOME/bee2evp/doc
# RUN bash build.sh
#RUN bash ./openssl.sh
#ENV PREFIX $HOME/bee2evp/build/local
#ENV LD_LIBRARY_PATH "${PREFIX}/lib:${LD_LIBRARY_PATH:-}"
#ENV PATH ${PREFIX}/bin:${PATH}
#RUN apt-get install echo -y -q
#WORKDIR /backend

#COPY requirements.txt /backend
#RUN pip3 install --upgrade pip -r requirements.txt
#RUN apt-get install vim -y -q

#COPY . /backend

#EXPOSE 443
#ENTRYPOINT [ "python3", "app.py" ]