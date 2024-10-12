FROM ubuntu:22.04

RUN echo "Первый образ докера в моей жизни"

RUN apt-get update && \
    apt-get install -y python3

COPY main.py /home/main.py

CMD "./main.py"

