FROM python:latest

RUN apt-get update && apt-get install -y git

ENV SQUARE_SIDE=4

RUN mkdir /app

COPY script.py /app

RUN mkdir /volume

VOLUME /volume

WORKDIR /volume

RUN git clone https://github.com/smartiqaorg/geometric_lib.git

WORKDIR /app

CMD ["python", "script.py"]





