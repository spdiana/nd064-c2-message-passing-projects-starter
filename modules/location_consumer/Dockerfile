FROM python:3.7-alpine

WORKDIR .

COPY . .
RUN pip install -r requirements.txt

EXPOSE 5004

COPY . .
ENTRYPOINT ["python", "person_kafka_consumer.py"]