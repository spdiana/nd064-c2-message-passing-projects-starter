import json
import os

from kafka import KafkaConsumer

# DB_USERNAME = os.environ["DB_USERNAME"]
# DB_PASSWORD = os.environ["DB_PASSWORD"]
# DB_HOST = os.environ["DB_HOST"]
# DB_PORT = os.environ["DB_PORT"]
# DB_NAME = os.environ["DB_NAME"]
# KAFKA_URL = os.environ["KAFKA_URL"]
# TOPIC_NAME = os.environ["KAFKA_TOPIC"]


DB_USERNAME = "postgres"
DB_PASSWORD = "docker"
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "postgres"
KAFKA_URL = "localhost:9092"
TOPIC_NAME = "quickstart-events"

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=[KAFKA_URL])


def persist_location_on_db(person):
    from sqlalchemy import create_engine

    engine = create_engine(f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True)
    conn = engine.connect()

    person_id = int(person["person_id"])
    latitude, longitude = float(person["latitude"]), float(person["longitude"])

    insert = "INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}))" \
        .format(person_id, latitude, longitude)

    print(insert)
    conn.execute(insert)


for location in consumer:
    message = location.value.decode('utf-8')
    print('{}'.format(message))
    location_message = json.loads(message)
    persist_location_on_db(location_message)
