FROM debian:latest
MAINTAINER johnnylingo
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt upgrade -y
RUN apt -y install apache2 apache2-doc libapache2-mod-wsgi-py3
RUN ln -s /etc/apache2/mods-available/headers.load /etc/apache2/mods-enabled/
RUN rm /etc/apache2/sites-enabled/000-default.conf
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN apt -y install python3-pip
RUN pip3 install paste python-multipart pyyaml
RUN rm -Rf /var/lib/apt/lists/*
COPY _default_.conf /etc/apache2/sites-enabled/
CMD apachectl -DFOREGROUND
EXPOSE 80 443
