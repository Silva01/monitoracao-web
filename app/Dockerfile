FROM python:2.7.14-slim-stretch

RUN mkdir -p /service
WORKDIR /service

COPY . /servic
RUN pip install --upgrade pipe
RUN pip install -r requirements.txt

ENV FLASK_APP=src/api.py
ENV COMPLEMENTO=Teste
EXPOSE 5000

ENTRYPOINT ["sh", "-c" ,"flask run --host=0.0.0.0"]
