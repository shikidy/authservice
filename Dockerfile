FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY alembic.ini .
COPY alembic/ alembic/

COPY src/ src/
COPY app.py .
COPY .env .

CMD ["/bin/sh", "-c", "alembic upgrade head && uvicorn app:app --host 0.0.0.0 --port 8000"]