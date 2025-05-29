import json
from kafka import KafkaConsumer

# Initialize Kafka consumer
consumer = KafkaConsumer(
    'air_quality',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  # Start reading at the earliest available message
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Starting consumer...")

# Continuously listen for messages
for message in consumer:
    data = message.value
    print(f"Received message: {data}")
    
    # Check if PM2.5 data exists and if it exceeds the threshold
    pm25 = data.get('PM2.5')  # Adjust the key name based on your CSV file headers
    if pm25 is not None:
        try:
            # Convert PM2.5 value to float for comparison
            if float(pm25) > 150:
                print("ALERT: PM2.5 level is very unhealthy!")
        except ValueError:
            print("Warning: PM2.5 value is not numeric.")
