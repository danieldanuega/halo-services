FROM python:3.7-slim as builder
RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean
WORKDIR /app
COPY . /app