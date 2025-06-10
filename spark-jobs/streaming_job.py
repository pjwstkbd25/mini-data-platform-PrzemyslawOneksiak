from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.avro.functions import from_avro
import requests
import time

# Schema Registry URL i lista tabel
schema_registry_url = "http://schema-registry:8081"
tables = ["table1", "table2", "table3"]

# Subscribe pattern na wszystkie trzy tabele
topic_pattern = "bigdata\\.public\\.(table1|table2|table3)"

# Pobieramy schemat dla pierwszej tabeli (zakładamy, że wszystkie mają tę samą strukturę)
subject = f"bigdata.public.{tables[0]}-value"
url = f"{schema_registry_url}/subjects/{subject}/versions/latest"

# Czekanie na pojawienie się schematu
print(f"Waiting for schema {subject} in Schema Registry...")
while True:
    resp = requests.get(url)
    if resp.status_code == 200:
        avro_schema = resp.json()["schema"]
        print(f"Schema for {subject} found.")
        break
    else:
        print(f"Schema not yet available ({resp.status_code}), retrying in 5s...")
        time.sleep(5)

# Spark z Delta Lake
spark = SparkSession.builder \
    .appName("KafkaAvroToDeltaStreaming") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# Czytanie ze wszystkich trzech tematów
df_raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribePattern", topic_pattern) \
    .option("startingOffsets", "earliest") \
    .load()

# Deserializacja AVRO i dodanie kolumny topic
df_parsed = df_raw.select(
    from_avro(col("value"), avro_schema).alias("data"),
    col("topic")
).select("data.*", "topic")

# Zapis do Delta Lake na MinIO
output_path = "s3a://delta/streaming_output"
checkpoint_path = "/opt/spark/checkpoints/streaming_job"

streaming_query = df_parsed.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", checkpoint_path) \
    .option("path", output_path) \
    .start()

streaming_query.awaitTermination()
