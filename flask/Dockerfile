FROM python:3.9-slim

RUN apt-get update 
RUN apt-get -y install libpq-dev gcc
RUN apt-get -y install curl

COPY ./app.py app.py

ENV  FLASK_APP=app.py

COPY ./requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "gunicorn","--workers","3","--bind","0.0.0.0:5000","wsgi:app" ]
