import time
import json
import pandas as pd
from kafka import KafkaProducer

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Path to CSV file (adjust the path as necessary)
csv_file = 'station_hour.csv'

# Read CSV data using pandas (modify 'nrows' to limit the number of rows)
data = pd.read_csv(csv_file, nrows=20)  # reading first 20 rows as an example

# Iterate over rows and send to Kafka topic
for index, row in data.iterrows():
    # Convert the row to a dictionary so that it can be serialized to JSON
    message = row.to_dict()
    
    # Send the message to Kafka topic 'air_quality'
    producer.send('air_quality', value=message)
    
    # Log what is sent for verification
    print(f"Sent message: {message}")
    
    # Sleep for 1 second to simulate real-time streaming
    time.sleep(1)

producer.flush()  # Ensure all messages are sent
producer.close()
