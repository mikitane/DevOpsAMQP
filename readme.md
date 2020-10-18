# Benefits of topic-based-communication compared to request-response (HTTP)
Topic-based-communication enables scaling in much more convenient way. When using topic-based-communication, sender and receiver don't have to know anything about each other. One just publishes messages to the topic and other consumes. This allows easy load balancing as new senders and receivers can be added dynamically. If one of the receivers goes down, another one can take its place.

Request-response-communication requires that sender knows the address of the receiver. This makes sender and receiver tightly coupled.

# Main learnings
I have previously used RabbitMQ with Celery, therefore the concepts of AMQP were familiar to me already. I learned to use pika library. I also learned that it is not possible to deliver same message to multiple consumers. Therefore the output of the Observer Service can vary between runs. Sometimes Intermediate Service receives the message from queue my.o and sometimes the message is received by Observer Service. More info here: https://stackoverflow.com/questions/10620976/rabbitmq-amqp-single-queue-multiple-consumers-for-same-message


