from ubuntu:18.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update \
        && apt install python3-pip -y \
        && pip3 install --upgrade pip \
        && apt-get install libmysqlclient-dev -y \
        && apt install python3-flask -y \
        && pip3 install python-socketio \
        && pip3 install gunicorn \
        && pip3 install flask flask_restful flask_mysqldb

WORKDIR /var/www/flaskapp
COPY . /var/www/flaskapp