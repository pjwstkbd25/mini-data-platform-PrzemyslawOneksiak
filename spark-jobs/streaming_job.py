from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

spark = SparkSession.builder \
    .appName("KafkaStreamingJob") \
    .getOrCreate()

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "bigdata-topic") \
    .load()

df_parsed = df.selectExpr("CAST(value AS STRING) as json_value")

query = df_parsed.writeStream \
    .format("console") \
    .option("truncate", False) \
    .start()

query.awaitTermination()