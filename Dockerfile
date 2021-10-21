FROM python:3-alpine3.9

RUN pip install qrcode

RUN pip install pyTelegramBotAPI

RUN pip install black

COPY . /app

WORKDIR /app

RUN pipenv install --deploy --dev

ENV SHELL=/bin/bash

ENTRYPOINT ["pipenv", "run"]

CMD        ["python"]