FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -
RUN apt-get install -y nodejs

WORKDIR /opt/dixit
COPY . .

RUN npm install

RUN pip install -r requirements-dev.txt
RUN python setup.py develop
