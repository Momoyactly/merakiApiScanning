FROM python:3.9-slim

RUN apt-get update 
RUN apt-get -y install libpq-dev gcc
RUN apt-get -y install curl
RUN pip install psycopg2 

COPY ./app.py app.py

ENV  FLASK_APP=app.py

COPY ./requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python","-m","flask","run","--host=0.0.0.0" ]
