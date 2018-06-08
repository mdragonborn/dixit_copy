FROM python:3.6
WORKDIR /usr/local/dixit
COPY . .
RUN pip install -r requirements-dev.txt
RUN python setup.py develop
