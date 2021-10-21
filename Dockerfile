FROM python:3-alpine3.9

RUN pip install qrcode

RUN pip install pyTelegramBotAPI

RUN pip install pytest

RUN pip install Pillow

COPY . /app

WORKDIR /app

ENV SHELL=/bin/bash

CMD ["python"]

ENV PYTHONPATH=.

CMD python botMain.py --port=$PORT  #port receiving

