import grpc

import person_kafka_event_pb2
import person_kafka_event_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = person_kafka_event_pb2_grpc.PersonEventItemServiceStub(channel)

# Update this with desired payload
person1 = person_kafka_event_pb2.PersonEventMessage(
    person_id=1,
    latitude=-35.0585136,
    longitude=106.5719521
)

person2 = person_kafka_event_pb2.PersonEventMessage(
    person_id=1,
    latitude=-35.0585136,
    longitude=106.5719521
)

response_1 = stub.Create(person1)
response_2 = stub.Create(person2)


print("Coordinates sent...")
print(person1, person2)
