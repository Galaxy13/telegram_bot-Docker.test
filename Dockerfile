FROM python:3

RUN pip install --upgrade pip

RUN pip install qrcode

RUN pip install pyTelegramBotAPI

RUN pip install pytest

RUN pip install Pillow==8.3.1

COPY . /app

WORKDIR /app

ENV SHELL=/bin/bash

CMD ["python"]

ENV PYTHONPATH=.

CMD python botMain.py --port=44158  #port receiving

