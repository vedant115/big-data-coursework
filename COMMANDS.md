# 📘 Big Data Lab Commands Reference

This file serves as a centralized reference of useful commands across all lab assignments. It covers usage of HDFS, Hadoop MapReduce, Streaming, Pig, Hive, Mahout, and Kafka.

---

## 📁 HDFS Commands

```bash
# Create directory
hdfs dfs -mkdir /folder_name

# Create nested directories
hdfs dfs -mkdir -p /path/with/nested/folders

# Upload files from local to HDFS
hdfs dfs -put /local/path/to/file /hdfs/target/path

# List files in HDFS
hdfs dfs -ls /path/to/dir

# View file content
hdfs dfs -cat /path/to/file

# Remove files or directories
hdfs dfs -rm -r /path/to/delete

# Download file from HDFS to local
hdfs dfs -get /hdfs/path /local/path
```
---

## 🛠️ Hadoop MapReduce (Java)
```bash
# Compile Java code
javac -classpath `hadoop classpath` -d . *.java

# Create a JAR file
jar -cvf myjob.jar -C . .

# Run MapReduce job
hadoop jar myjob.jar ClassName /input/path /output/path
```
---

## 🐍 Hadoop Streaming (Python)
```bash
# Run Python-based Hadoop Streaming job
hadoop jar /home/vedant/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar \
  -input /LabAssign4/input/TbDiseaseSymptoms.csv \
  -output /LabAssign4/output \
  -mapper tb_mapper.py \
  -reducer tb_reducer.py \
  -file tb_mapper.py \
  -file tb_reducer.py
```
---

## 🐷 Apache Pig
```bash
# Load CSV data
healthcare_data = LOAD '/Healthcare_Assign/input/healthcare_dataset.csv' 
USING PigStorage(',') AS (
    Name:chararray, Age:int, Gender:chararray, BloodType:chararray, 
    MedicalCondition:chararray, DateOfAdmission:chararray, Doctor:chararray, 
    Hospital:chararray, InsuranceProvider:chararray, BillingAmount:float, 
    RoomNumber:int, AdmissionType:chararray, DischargeDate:chararray, 
    Medication:chararray, TestResults:chararray
);

# Filter rows
filtered_data = FILTER healthcare_data BY MedicalCondition == 'Diabetes';

# Group data by gender
grouped_data = GROUP filtered_data BY Gender;

# Display results
DUMP grouped_data;
```
---

## 🐝 Apache Hive
```bash
# Connect using Beeline
beeline -u jdbc:hive2://

# Create table
CREATE TABLE healthcare (
  Name STRING, Age INT, Gender STRING, BloodType STRING, MedicalCondition STRING,
  DateOfAdmission STRING, Doctor STRING, Hospital STRING, InsuranceProvider STRING,
  BillingAmount FLOAT, RoomNumber INT, AdmissionType STRING, DischargeDate STRING,
  Medication STRING, TestResults STRING
)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' 
STORED AS TEXTFILE;

# Load data into table
LOAD DATA INPATH '/Healthcare_Assign/input/healthcare_dataset.csv' INTO TABLE healthcare;

# Query data
SELECT * FROM healthcare WHERE MedicalCondition = 'Diabetes';
```
---

## 🧮 Apache Mahout
```bash
# Convert CSV to sequence file
mahout seqdirectory \
  -i hdfs://localhost:9000/LabAssign6/input/diabetes.csv \
  -o hdfs://localhost:9000/LabAssign6/input/diabetes.seq \
  -c UTF-8

# Convert sequence file to sparse vector
mahout seq2sparse \
  -nv \
  -i hdfs://localhost:9000/LabAssign6/input/diabetes.seq \
  -o hdfs://localhost:9000/LabAssign6/output/diabetes-vectors-sparse \
  --maxDFPercent 85 \
  --namedVector

# Train a Naive Bayes classifier
mahout trainnb \
  -i diabetes-vectors-sparse/tfidf-vectors \
  -o model \
  -li labelindex \
  -ow

# Test the classifier
mahout testnb \
  -i diabetes-vectors-sparse/tfidf-vectors \
  -m model \
  -l labelindex \
  -ow \
  -o result
```
---

## 🔃 Apache Kafka
```bash
# Create a topic
kafka-topics.sh --create --topic tb_risk_stream --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# Start a producer (Python)
python3 producer.py

# Start a consumer (Python)
python3 consumer.py
```