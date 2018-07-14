# coding: utf-8

"""
    Simple web application to get request and publish in a kafka topic.
"""
from flask import Flask
from kafka import KafkaProducer

app = Flask(__name__)


@app.route("/")
def home():
    # https://github.com/dpkp/kafka-python#kafkaproducer
    producer = KafkaProducer(bootstrap_servers='kafka:9092')
    producer.send('notification', b'some_message_bytes')
    producer.flush()

    return "A new topic was published."


if __name__ == "__main__":
    app.run(port=5001, host="0.0.0.0")
