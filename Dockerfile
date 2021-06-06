#Here I am adding python 3
FROM python:3.7
#Here I create a file in the container called app
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY ./requirements.txt ./requirements.txt

RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt

ADD . /code