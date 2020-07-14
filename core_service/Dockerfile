FROM python:3.7-slim as builder
RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --user -r requirements.txt

FROM python:3.7-slim as runner
RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get install libsm6 libxext6 libglib2.0-0 libxrender-dev -y \
    && apt-get clean
COPY --from=builder /root/.local /root/.local
COPY . /app
WORKDIR /app
ENV PATH=/root/.local/bin:$PATH
EXPOSE 9000
ENTRYPOINT ["python", "server.py"]
