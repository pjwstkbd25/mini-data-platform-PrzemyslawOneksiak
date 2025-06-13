from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError
print("Starting")
conf = {
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest',
    'schema.registry.url': 'http://schema-registry:8081'
}

consumer = AvroConsumer(conf)
consumer.subscribe(['test.public.table3', 'test.public.table2', 'test.public.table1'])

try:
    while True:
        try:
            msg = consumer.poll(1.0)
            if msg is None:
                print("No message")
                continue
            print(f"Key: {msg.key()}, Value: {msg.value()}")
        except SerializerError as e:
            print("Message deserialization failed:", e)
finally:
    print("Stopping")
    consumer.close()