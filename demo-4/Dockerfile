FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN useradd -m appuser
WORKDIR /app

RUN pip install --no-cache-dir flask

COPY app.py /app/

EXPOSE 8000

USER appuser

CMD ["python", "app.py"]