FROM debian:bullseye-slim
MAINTAINER johnnylingo
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y
RUN apt-get -y install apache2 apache2-doc libapache2-mod-wsgi-py3
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN rm -Rf /var/lib/apt/lists/*
RUN ln -s /etc/apache2/mods-available/headers.load /etc/apache2/mods-enabled/
RUN rm /etc/apache2/sites-enabled/000-default.conf
COPY _default_.conf /etc/apache2/sites-enabled/
COPY mod_wsgi.conf /etc/apache2/conf-enabled/
CMD apachectl -DFOREGROUND
EXPOSE 80 443
