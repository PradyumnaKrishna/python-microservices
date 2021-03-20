from time import sleep
import pika
import json

# time to boot
sleep(15)

params = pika.URLParameters('amqp://guest:guest@my-rabbit:5672/')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main',
                          body=json.dumps(body), properties=properties)
