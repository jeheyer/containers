FROM ubuntu:latest
MAINTAINER johnnylingo
ARG DEBIAN_FRONTEND=noninteractive
ENV APACHE_CFG_DIR=/etc/apache2
ENV BIND_CFG_DIR=/etc/bind
ENV BIND_LOG_DIR=/var/log/named
RUN apt update && apt upgrade -y
RUN apt -y install apache2 apache2-doc libapache2-mod-wsgi-py3 bind9
RUN ln -s /etc/apache2/mods-available/headers.load /etc/apache2/mods-enabled/
RUN rm /etc/apache2/sites-enabled/000-default.conf
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN apt -y install python3-pip
RUN pip3 install paste python-multipart
RUN rm -Rf /var/lib/apt/lists/*
COPY mod_wsgi.conf $APACHE_CFG_DIR/conf-enabled/
COPY _default_.conf $APACHE_CFG_DIR/sites-enabled/
CMD apachectl -DFOREGROUND
COPY debian.conf.options $BIND_CFG_DIR
COPY named.conf.local $BIND_CFG_DIR
COPY tokens_dudewheresmydns_com.txt /var/cache/bind/
RUN mkdir -p BIND_LOG_DIR
RUN chown bind:bind BIND_LOG_DIR
COPY bind9 /etc/default/
CMD named -g
EXPOSE 80 53
