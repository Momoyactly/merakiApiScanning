FROM python:3.9-alpine

COPY ./app.py app.py

ENV  FLASK_APP=app.py

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python","-m","flask","run","--host=0.0.0.0" ]
