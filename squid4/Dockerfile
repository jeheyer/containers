FROM debian:buster
MAINTAINER johnnylingo
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y
RUN apt-get install squid -y
RUN rm -Rf /var/lib/apt/lists/*
ENV CFG_DIR=/etc/squid
ENV LOG_DIR=/var/log/squid
COPY squid.conf $CFG_DIR
CMD service squid stop && squid -z
CMD ["service", "squid", "start"]
ENV PORT=3128
EXPOSE $PORT
