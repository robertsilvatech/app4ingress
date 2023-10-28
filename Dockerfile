FROM python:3.10-slim

COPY requirements.txt /
RUN pip install -U pip && pip install -r requirements.txt

COPY main.py /app/main.py
EXPOSE 8000

WORKDIR /app

CMD uvicorn main:app --host 0.0.0.0 --port 8000 --reload