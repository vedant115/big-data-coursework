import json
import logging
import random  # For simulating age if not provided in data
from kafka import KafkaConsumer

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('tb_risk_logger')
# Optionally, add FileHandler to log to a file:
# file_handler = logging.FileHandler("alerts.log")
# logger.addHandler(file_handler)

# Create Kafka Consumer instance.
consumer = KafkaConsumer(
    'tb_risk_stream',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def calculate_risk_score(data):
    """
    Compute risk score from given data using the weights:
      - Fever: 1 point (from "fever for two weeks")
      - Cough: 1 point (using "coughing blood"; you can change this to a different column)
      - Fatigue: 1 point (from "body feels tired")
      - Weight Loss: 1 point (from "weight loss")
      - Chest Pain: 1 point (from "chest pain")
      - Shortness of Breath: 1 point (from "shortness of breath")
    """
    try:
        # Convert string values to integers (assuming CSV stores them as 0/1)
        fever = int(data.get("fever for two weeks", 0))
        cough = int(data.get("coughing blood", 0))
        fatigue = int(data.get("body feels tired", 0))
        weight_loss = int(data.get("weight loss", 0))
        chest_pain = int(data.get("chest pain", 0))
        shortness_of_breath = int(data.get("shortness of breath", 0))
    except Exception as e:
        logger.error("Error parsing symptoms: %s", e)
        return 0, weight_loss  # Return default if error

    total_score = fever + cough + fatigue + weight_loss + chest_pain + shortness_of_breath
    return total_score, weight_loss

def raise_alerts(data, total_score, weight_loss):
    alerts = []
    # Alert 1: High TB Risk
    if total_score > 7:
        alerts.append("High TB Risk")
    
    # Simulate an age value if not available in the CSV (e.g., between 10 and 70)
    # In a real scenario, use the actual age from your dataset.
    age = int(data.get("age", random.randint(10, 70)))

    # Alert 2: Unusual case: risk score > 4 and young age (< 20)
    if total_score > 4 and age < 20:
        alerts.append("Unusual Case: Young Age with Symptoms")
    
    # Alert 3: Unexpected Weight Loss
    # Check if the patient is male, has weight loss = yes, and no other symptoms.
    try:
        gender = data.get("gender", "").lower()
        # Collect other symptom scores
        other_symptoms = sum([
            int(data.get("fever for two weeks", 0)),
            int(data.get("coughing blood", 0)),
            int(data.get("body feels tired", 0)),
            int(data.get("chest pain", 0)),
            int(data.get("shortness of breath", 0))
        ])
    except Exception as e:
        logger.error("Error parsing gender or symptoms: %s", e)
        gender, other_symptoms = "", 0
    
    if gender == "male" and other_symptoms == 0 and weight_loss == 1:
        alerts.append("Unexpected Weight Loss")
    
    return alerts, age

logger.info("Consumer is starting and waiting for messages...")

# Consume messages continuously.
for message in consumer:
    data = message.value
    total_score, weight_loss = calculate_risk_score(data)
    alerts, age = raise_alerts(data, total_score, weight_loss)
    logger.info("Received data: %s", data)
    logger.info("Calculated TB Risk Score: %d", total_score)
    
    # Log any alerts
    if alerts:
        for alert in alerts:
            alert_message = f"Alert for patient {data.get('name', 'Unknown')}: {alert} (Score: {total_score}, Age: {age})"
            logger.warning(alert_message)
    else:
        logger.info("No alerts for this record.")
