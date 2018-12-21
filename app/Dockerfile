FROM python:2.7.14-slim-stretch

RUN mkdir -p /service
WORKDIR /service

COPY . /service
RUN pip install -r requirements.txt

ENV FLASK_APP=src/api.py
EXPOSE 5000

ENTRYPOINT ["sh", "-c" ,"flask run --host=0.0.0.0"]
