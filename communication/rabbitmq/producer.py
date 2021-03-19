import pika
import json


def send_sensor(sensor, temperature, huminity):
    S = sensor
    T = temperature
    H = huminity

    credentials = pika.PlainCredentials('user', 'user')
    params = pika.ConnectionParameters('rabbit', 5672, '/', credentials)
    connection = pika.BlockingConnection(params)

    channel = connection.channel()

    channel.queue_declare(queue="hello")

    body = {'S': S, 'T': T, 'H': H}

    channel.basic_publish(exchange='',
                          routing_key="hello",
                          body=json.dumps(body))
    print(" [x] Sent 'Sensor!'")

    connection.close()
