from confluent_kafka import Consumer, KafkaException
from confluent_kafka.admin import AdminClient
import time

consumer_conf = {
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'debezium-consumer-group',
    'auto.offset.reset': 'earliest'
}

topics = ['bigdata.public.table1', 'bigdata.public.table2', 'bigdata.public.table3']


admin = AdminClient({'bootstrap.servers': consumer_conf['bootstrap.servers']})
for topic in topics:
    for _ in range(12):
        md = admin.list_topics(timeout=55)
        if topic in md.topics and not md.topics[topic].error:
            print(f"Topic {topic} is now available")
            break
        print(f"Waiting for topic {topic}...")
        time.sleep(15)
    else:
        raise Exception(f"Topic {topic} did not appear")

consumer = Consumer(consumer_conf)
consumer.subscribe(topics)

try:
    while True:
        msg = consumer.poll(3.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())
        print(f"[{msg.topic()}] {msg.value().decode('utf-8')}")
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
