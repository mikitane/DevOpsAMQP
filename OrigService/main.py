import pika
import time
from datetime import datetime

BROKER_NAME = 'broker_service'
EXCHANGE = ''
QUEUE = 'my.o'

def establish_connection(retries=0):
    try:
        return pika.BlockingConnection(pika.ConnectionParameters(BROKER_NAME))
    except pika.exceptions.AMQPConnectionError as e:
        if retries > 10:
            raise e

        time.sleep(2)
        return establish_connection(retries=retries + 1)

def main():
    connection = establish_connection()
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE)

    for i in range(1, 4):
        message = 'MSG_{}'.format(i)

        channel.basic_publish(exchange=EXCHANGE,
                            routing_key=QUEUE,
                            body=message)

        print('Message sent: ', message)
        time.sleep(3)

    connection.close()

# Start the service
main()
