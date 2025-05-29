# Lab Task 4

## 📘 Assignment Overview

This lab involves analyzing a tuberculosis (TB) dataset using Hadoop MapReduce. The focus is on implementing a MapReduce job to extract and aggregate TB symptoms and monitoring the performance and execution flow using the JobTracker interface.

---

## 🧠 Objectives

- Process a multi-file dataset to extract key TB-related symptoms using MapReduce.
- Aggregate the data to uncover symptom frequency or pattern trends.
- Monitor and evaluate the job's performance via Hadoop's JobTracker.

---

## ⚙️ Task Details

### Dataset Source

- **Dataset:** `Tb disease symptoms.csv` from  
  [Kaggle - Tuberculosis Symptoms Dataset](https://www.kaggle.com/datasets/victorcaelina/tuberculosis-symptoms)
- **Note:** The dataset contains multiple CSV files.

### MapReduce Job

1. **Mapper**
   - Extract key symptoms and associated patient information from each line.

2. **Reducer**
   - Aggregate the data to find counts or patterns of specific symptoms.

### Execution Instructions

a. Upload the dataset (`Tb disease symptoms.csv`) to HDFS.  
b. Submit the MapReduce job using the Hadoop CLI.  
c. Monitor job progress using the **JobTracker web interface**.

---

## 🛠️ Technologies Used

- Apache Hadoop (MapReduce)
- Java or Python
- HDFS
- Hadoop JobTracker (for job monitoring)

---
