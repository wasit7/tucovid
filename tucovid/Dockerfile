FROM python:3.7-slim
RUN apt update
RUN apt install git -y

WORKDIR /tucovid
ADD ./requirements.txt /tucovid/requirements.txt
RUN pip install -r /tucovid/requirements.txt
ADD . /tucovid/
