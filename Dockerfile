FROM python:3-alpine3.9

RUN pip install qrcode

RUN pip install pyTelegramBotAPI

COPY . /app

WORKDIR /app

RUN pipenv install --deploy --dev

ENV SHELL=/bin/bash

ENTRYPOINT ["pipenv", "run"]

CMD        ["python"]