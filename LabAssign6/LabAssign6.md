# Lab Task 6

## 📘 Assignment Overview

This lab involves using **Apache Mahout** to perform both **classification** and **clustering** on a diabetes dataset. You will build a **Naive Bayes classifier** to predict diabetes cases and apply **K-Means clustering** to uncover natural groupings within the data. The assignment includes steps for data preprocessing, model training, evaluation, and reporting.

---

## 🧠 Objectives

- Use **Apache Mahout** for supervised (Naive Bayes) and unsupervised (K-Means) learning tasks.
- Train and test models on a dataset uploaded to HDFS.
- Evaluate model performance using standard metrics.
- Compare and interpret results from classification and clustering techniques.

---

## 📂 Dataset

- **Name:** `diabetes.csv`
- **Source:** [GitHub - Plotly Datasets](https://github.com/plotly/datasets/blob/master/diabetes.csv)
- **Storage:** Upload to HDFS

---

## ⚙️ Task Breakdown

### 🔧 Preprocessing Steps

1. **Upload** `diabetes.csv` to HDFS.
2. **Convert** the CSV file to a **SequenceFile** format suitable for Mahout.
3. **Split** the `.seq` file:
   - **Training Set:** 70%
   - **Test Set:** 30%

---

### 🧪 Classification (Naive Bayes)

- **Training:** Train a Naive Bayes classifier on the training data.
- **Testing:** Predict outcomes using the test set.
- **Evaluation Metrics:**
  - Accuracy
  - Precision
  - Recall
  - Confusion Matrix

---

### 📊 Clustering (K-Means)

- **Preprocessing:** Convert the dataset into **Mahout vector format**.
- **Clustering:** Apply K-Means on vectorized data.
- **Evaluation Metrics:**
  - **Inter-cluster distance:** Distance between cluster centers.
  - **Intra-cluster distance:** Average distance between points within a cluster.

---

## 📈 Final Report Requirements

- Performance summary of the **Naive Bayes classifier**:
  - Confusion Matrix
  - Accuracy, Precision, Recall
- Analysis of **K-Means clustering quality**:
  - Inter-cluster vs. Intra-cluster distances
  - Interpretation of cluster distributions
- Comparative discussion:
  - Contrast classification vs. clustering performance
  - Insights about dataset structure and predictability

---

## 🛠️ Technologies Used

- Apache Mahout
- HDFS
- Hadoop CLI
- SequenceFile I/O
- Vector conversion tools (Mahout CLI)

---