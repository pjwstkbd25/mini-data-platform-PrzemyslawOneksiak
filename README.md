**Projekt zaliczeniowy na zajęcia BigData**  
**Autor: Przemysław Oneksiak s34225**

# **Mini Platforma Danych w Dockerze**


## Cel projektu

- Symulacja procesu biznesowego (Python + CSV)

- Przechowywanie i zarządzanie danymi w PostgreSQL

- CDC z Debezium → Kafka (AVRO + Schema Registry)

- Przetwarzanie strumieni w Spark Structured Streaming

- Zapis wyników jako pliki Delta w MinIO (S3‑compatible)

### Elementy i konfiguracja

- Simulator: Python czytający CSV, dynamiczne tworzenie tabel i INSERT do Postgresa.

- PostgreSQL: logical replication, Docker Secrets, healthcheck pg_isready.

- Debezium: Kafka Connect, AVRO, monitoruje zmiany w Postgresie.

- Kafka & Schema Registry: brokery + rejestr schematów dla AVRO.

- Spark: kontener z Delta‑Spark, Hadoop‑AWS, AWS CLI; Structured Streaming → Kafka → MinIO.

- MinIO: bucket delta, S3A, healthcheck mc ls local/delta.

### Uruchomienie

`docker-compose --profile=* up --build -d`

Konsola MinIO: http://localhost:9090

Spark UI: http://localhost:8080

