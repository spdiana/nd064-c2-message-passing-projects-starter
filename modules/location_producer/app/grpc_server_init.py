import time
import json
import logging
import grpc

import person_kafka_event_pb2
import person_kafka_event_pb2_grpc

from kafka import KafkaProducer
from concurrent import futures


# kafka_url = os.environ["KAFKA_URL"]
# kafka_topic = os.environ["KAFKA_TOPIC"]

kafka_url = "localhost:9092"
kafka_topic = "quickstart-events"

logging.info('connecting to kafka ', kafka_url)
print('p_connecting to kafka ', kafka_url)
logging.info('connecting to kafka topic ', kafka_topic)
print('p_connecting to kafka topic ', kafka_topic)

producer = KafkaProducer(bootstrap_servers=kafka_url)
# g.kafka_producer = producer


class KafkaEventServicer(person_kafka_event_pb2_grpc.PersonEventItemServiceServicer):

    def Create(self, request, context):
        request_value = {
            'person_id': int(request.person_id),
            'latitude': int(request.latitude),
            'longitude': int(request.longitude)
        }

        logging.info('creating event ', request_value)
        print(request_value)

        user_encode_data = json.dumps(request_value, indent=2).encode('utf-8')
        producer.send(kafka_topic, user_encode_data)
        producer.flush()
        return person_kafka_event_pb2.PersonEventMessage(**request_value)


server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
person_kafka_event_pb2_grpc.add_PersonEventItemServiceServicer_to_server(KafkaEventServicer(), server)

logging.info('Server starting on port 5005')
print('Server starting on port 5005')
server.add_insecure_port('[::]:5005')
server.start()

# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
