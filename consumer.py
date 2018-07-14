# coding: utf-8
from kafka import KafkaConsumer

"""
    Simple example of kafka consumer.
"""


class Consumer(object):

    def run(self):
        consumer = KafkaConsumer("notification", bootstrap_servers='kafka:9092')

        for msg in consumer:
            print(msg)


if __name__ == "__main__":
    (Consumer()).run()
