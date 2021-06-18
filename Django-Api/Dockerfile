FROM python:3.8
LABEL Alfredo Bolio

# setup environment variable  
ENV DockerHOME=/home/app/webapp  

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME 

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

#RUN adduser --disabled-password  user
#USER user

RUN useradd -ms /bin/bash newuser
USER newuser

EXPOSE 8000 