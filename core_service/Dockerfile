FROM python:3.7-slim as builder
RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get install libsm6 libxext6 libglib2.0-0 libxrender-dev -y \
    && apt-get clean
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
