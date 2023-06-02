FROM python:3.8-alpine

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY __init__.py .
COPY app.py .

RUN chmod +x /app.py
