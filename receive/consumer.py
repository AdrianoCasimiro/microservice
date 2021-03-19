import pika
import sys
import os
import psycopg2
import json


def main():
    credentials = pika.PlainCredentials('user', 'user')
    params = pika.ConnectionParameters('rabbit', 5672, '/', credentials)
    connection = pika.BlockingConnection(params)

    channel = connection.channel()


    def store(ch, method, properties, body):
        body = json.loads(body)
        print("[X] Received Sensor:" + str(body["S"]) +
              " temperature: " + str(body["T"]) +
              " Umidade: " + str(body["H"]))

        print(body["S"])
        try:
            # up.uses_netloc.append("postgres")
            # url = up.urlparse(
            # os.environ['postgres://msutlqhlgtyfha:0dcb1223d906388dabdeee4f8bab89182340147dd35473c1795ee9fc98651c2f@ec2-174-129-194-188.compute-1.amazonaws.com:5432/d10cs7ffhbaufp'])
            conn_string = "host ='db' dbname='hello_flask_dev' user='hello_flask' password='hello_flask'"
            print("Connecting to database\n	->%s" % (conn_string))
            connection = psycopg2.connect(conn_string)
            cursor = connection.cursor()
            print('teste')
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS sensor (id SERIAL PRIMARY KEY, S VARCHAR, T integer, H integer);")
            print('create table')
            postgres_insert_query = """ INSERT INTO sensor (S, T, H) VALUES (%s,%s,%s)"""
            print('postgres_insert_query')
            record_to_insert = ((body["S"]),
                                int(body["T"]),  int(body["H"]))
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
            print('commit')
            count = cursor.rowcount
            print(count, "Record inserted successfully into sensor table")

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            # closing database connection.
            if(connection):
                connection.close()
                print("PostgreSQL connection is closed")

    channel.basic_consume(
        queue="hello", on_message_callback=store, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
