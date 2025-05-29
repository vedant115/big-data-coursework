# Lab Assignment 7

## 📘 Assignment Overview

This lab focuses on using **Apache Spark** and **GraphX** for graph-based analysis of tuberculosis symptom data. The dataset is converted to RDF format and loaded into Spark to build a graph, on which several key graph algorithms are applied to extract insights and optimize performance.

---

## 🧠 Objectives

- Convert the tuberculosis symptoms dataset into RDF format using **RDFLib**.
- Load RDF data into Spark and construct a **GraphX** graph.
- Perform graph operations to analyze disease and symptom relationships.
- Measure execution time and monitor memory usage of Spark jobs.

---

## 📂 Dataset

- **Dataset:** `Tb disease symptoms.csv`  
- **Source:** [Kaggle - Tuberculosis Symptoms Dataset](https://www.kaggle.com/datasets/victorcaelina/tuberculosis-symptoms?select=Tb+disease+symptoms.csv)

---

## ⚙️ Task Breakdown

### Part 1: RDF Conversion

- Convert the CSV dataset into **RDF format** using the Python library **RDFLib**.

### Part 2: Load and Graph Creation

- Load the RDF data into **Apache Spark**.
- Create a **GraphX graph** representation of the data.

### Part 3: Graph Operations

- **PageRank:** Identify influential diseases or symptoms based on graph connectivity.
- **Community Detection:** Cluster diseases, symptoms, and treatments into related groups.
- **Connected Components:** Detect isolated groups within the graph.
- **Shortest Path:** Calculate the shortest path between any two diseases or risk factors.

### Performance Monitoring

- Measure execution time for each graph operation.
- Monitor memory consumption of Spark jobs, especially with large datasets.

---

## 🛠️ Technologies Used

- Apache Spark (GraphX)
- Python (RDFLib)
- Hadoop/HDFS (for dataset storage)
- Scala/Java (Spark GraphX jobs)

---