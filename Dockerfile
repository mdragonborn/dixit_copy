FROM python:3.6
ENV PYTHONUNBUFFERED 1
WORKDIR /opt/dixit
COPY . .
RUN pip install -r requirements-dev.txt
RUN python setup.py develop
