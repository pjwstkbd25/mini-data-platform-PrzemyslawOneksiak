from confluent_kafka import Consumer, KafkaException

consumer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'debezium-consumer-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_conf)
topic = 'test'
consumer.subscribe([topic])

try:
    while True:
        msg = consumer.poll(3.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())
        print("Odebrano komunikat")
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
