FROM python:3.7.5-stretch

WORKDIR /flask

COPY . /flask

RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]