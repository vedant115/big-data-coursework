import csv
import json
import time
from kafka import KafkaProducer

# Define Kafka producer with JSON serialization.
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

csv_file = 'tuberculosis.csv'
topic = 'tb_risk_stream'

# Open the CSV file and stream each row as a JSON message.
with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Clean/adjust the keys if necessary (e.g., remove extra spaces)
        row = {key.strip(): value.strip() for key, value in row.items()}
        producer.send(topic, row)
        print(f"Sent record: {row}")
        time.sleep(1)  # Send one record per second

producer.flush()
producer.close()
