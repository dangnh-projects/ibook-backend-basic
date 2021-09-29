FROM python:3.8.2

ENV PYTHONUNBUFFERED=1
# create folder
RUN mkdir /code
# copy all to code folder
COPY . /code/
# use code folder
WORKDIR /code
# copy requirements to /code/ibook/
# COPY requirements.txt /code/ibook/
# setup env
RUN pip install -r ibook/requirements.txt
