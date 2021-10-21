FROM python:3-alpine3.9

RUN pip install qrcode

RUN pip install pyTelegramBotAPI

COPY . /app

WORKDIR /app

ENV SHELL=/bin/bash

CMD ["python"]

CMD python botMain.py --port=$PORT  #port receiving

