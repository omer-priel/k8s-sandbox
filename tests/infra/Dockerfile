FROM ubuntu:24.04

WORKDIR /app

RUN apt-get update
RUN apt-get install -y make
RUN apt-get install -y curl jq

COPY tests /app/tests

COPY Makefile /app/Makefile

ENTRYPOINT ["make", "test"]
