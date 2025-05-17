FROM python:3.10-slim

WORKDIR /app

COPY requirements-kafka.txt .
RUN pip install --no-cache-dir -r requirements-kafka-consumer.txt

COPY src/kafka/consumer.py .

ENTRYPOINT ["python", "consumer.py"]
