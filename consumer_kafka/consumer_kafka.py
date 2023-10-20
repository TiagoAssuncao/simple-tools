from confluent_kafka import Consumer, KafkaError

# Define your Kafka broker and topic
bootstrap_servers = 'localhost:9092'  # Update with your Kafka broker(s)
topic = 'myTopicName'  # Update with your topic name

# Create a Kafka consumer
conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'my-consumer-group',  # Specify your consumer group
    'auto.offset.reset': 'earliest',  # Start consuming from the beginning of the topic
}

consumer = Consumer(conf)

import ipdb

# Subscribe to the topic
consumer.subscribe([topic])

try:
    while True:
        msg = consumer.poll(1.0)  # Poll for messages every 1 second

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("Reached end of partition")
            else:
                print("Error while consuming message: {}".format(msg.error()))
        else:
            print("Reciving a msg")
            # Process the consumed message
            print("Received message: {}".format(msg.value().decode('utf-8')))
            print("Header message: {}".format(msg.value().decode('utf-8')))

except KeyboardInterrupt:
    pass
finally:
    consumer.close()

