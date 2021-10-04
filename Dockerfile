FROM python:3.8.3-alpine

ADD . /

WORKDIR /

RUN pip3 install -r requirements.txt

CMD [ "python3.8", "./manage.py", "runserver", "0.0.0.0:8000" ]
