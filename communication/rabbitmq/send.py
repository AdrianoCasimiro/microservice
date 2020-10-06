import pika
import os
import json


def send_sensor(sensor, temperature, huminity):
    S = sensor
    T = temperature
    H = huminity

    # url = os.environ.get(
    #    'CLOUDAMQP_URL', 'amqps://admin:admin@rabbit:5672/')
    credentials = pika.PlainCredentials('admin', 'admin')

    parameters = pika.ConnectionParameters('rabbit',
                                           5672,
                                           '/',
                                           credentials)

    connection = pika.BlockingConnection(parameters)
    #params = pika.URLParameters(url)
    #connection = pika.BlockingConnection(params)

    channel = connection.channel()

    channel.queue_declare(queue='hello')

    body = {'S': S, 'T': T, 'H': H}

    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=json.dumps(body))
    print(" [x] Sent 'Sensor!'")

    connection.close()
