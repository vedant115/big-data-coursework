# Lab Assignment 9

## 📘 Assignment Overview

This lab simulates real-time streaming of tuberculosis symptom data using **Apache Kafka**. The goal is to compute a TB risk score for each patient based on weighted symptoms and raise alerts for high-risk and anomalous cases.

---

## 🧠 Objectives

- Create a Kafka topic to stream TB symptom data.
- Develop a Kafka Producer to read CSV data, convert it to JSON, and stream it.
- Develop a Kafka Consumer to parse data, calculate TB risk scores, and generate alerts based on predefined rules.

---

## 📂 Dataset

- **Dataset:** `tuberculosis.csv`  
- **Source:** [Kaggle - Tuberculosis Symptoms Dataset](https://www.kaggle.com/datasets/victorcaelina/tuberculosis-symptoms)

---

## ⚙️ Instructions

### Step 1: Kafka Topic Creation

- Create a Kafka topic named: `tb_risk_stream`

### Step 2: Kafka Producer (`producer.py`)

- Read `tuberculosis.csv`.
- Convert each row to JSON format.
- Stream one row per second to the Kafka topic `tb_risk_stream`.

### Step 3: Kafka Consumer (`consumer.py`)

- Parse incoming JSON messages.
- Calculate a **TB Risk Score** using this weighting scheme (score range 0 to 12):

  | Symptom             | Weight |
  |---------------------|--------|
  | Fever               | 1 point|
  | Cough               | 1 point|
  | Fatigue             | 1 point|
  | Weight Loss         | 1 point|
  | Chest Pain          | 1 point|
  | Shortness of Breath | 1 point|

- Raise alerts based on the following rules:

  - Risk Score > 7 → **"High TB Risk"**
  - Risk Score > 4 and Age < 20 → **"Unusual Case: Young Age with Symptoms"**
  - Gender: Male with no symptoms but Weight Loss = Yes → **"Unexpected Weight Loss"**

- Log alerts to the console and optionally to an alert log file.

---

## 📎 Submission Requirements

- Screenshot of Kafka topic creation.
- Screenshot of Kafka Producer terminal output.
- Screenshot of Kafka Consumer terminal output showing alerts.
- Source code files:  
  - `producer.py`  
  - `consumer.py`

---

## 🛠️ Technologies Used

- Apache Kafka
- Python (for Producer and Consumer scripts)
