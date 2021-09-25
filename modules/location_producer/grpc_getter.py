import grpc
import person_kafka_event_pb2
import person_kafka_event_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = person_kafka_event_pb2_grpc.PersonEventItemServiceStub(channel)

response = stub.Get(person_kafka_event_pb2.Empty())
print(response)
