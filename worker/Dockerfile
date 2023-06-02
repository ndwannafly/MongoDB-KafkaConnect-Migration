FROM python:3.8-alpine

COPY requirements.txt .

RUN apk update && apk add --no-cache bash

RUN pip install -r requirements.txt
COPY __init__.py .
COPY run.sh .
COPY app.py .
RUN chmod +x /run.sh
RUN chmod +x /app.py
