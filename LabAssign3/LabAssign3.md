# Lab Assignment 3

## 📘 Assignment Overview

This lab focuses on performing various analytical tasks using Hadoop MapReduce on a healthcare dataset. The dataset includes multiple patient-related attributes such as age, gender, medical condition, admission dates, billing amount, and more. Students are required to implement specific MapReduce jobs to extract meaningful insights from this dataset.

---

## 🧠 Objectives

- Apply MapReduce techniques to extract, aggregate, and analyze structured healthcare data.
- Gain hands-on experience in writing custom Mappers and Reducers for real-world datasets.

---

## ⚙️ Task Details

### Dataset Source

- **Dataset URL:** [Kaggle - Healthcare Dataset](https://www.kaggle.com/datasets/prasad22/healthcare-dataset?resource=download)
- **Storage:** Upload the dataset to HDFS for processing.

### Columns in the Dataset

1. Name  
2. Age  
3. Gender  
4. Blood Type  
5. Medical Condition  
6. Date of Admission  
7. Doctor  
8. Hospital  
9. Insurance Provider  
10. Billing Amount  
11. Room Number  
12. Admission Type  
13. Discharge Date  
14. Medication  
15. Test Results  

---

## 🗂️ MapReduce Analysis Tasks

1. **Total Billing Amount per Hospital**
   - **Mapper:** Extract hospital name and billing amount.
   - **Reducer:** Sum billing amounts for each hospital.

2. **Average Length of Stay per Medical Condition**
   - **Mapper:** Calculate stay duration (Discharge Date - Admission Date) and emit with medical condition.
   - **Reducer:** Compute the average length of stay per condition.

3. **Most Common Medical Conditions per Age Group**
   - **Mapper:** Classify into age groups (0–18, 19–35, 36–50, 51+) and emit medical condition.
   - **Reducer:** Count conditions per age group and identify the most common ones.

4. **Most Prescribed Medications per Medical Condition**
   - **Mapper:** Emit medical condition and prescribed medication.
   - **Reducer:** Count medication frequency per condition.

5. **Average Billing Amount per Insurance Provider**
   - **Mapper:** Emit insurance provider and billing amount.
   - **Reducer:** Calculate average billing per provider.

6. **Admission Type Distribution per Hospital**
   - **Mapper:** Emit hospital name and admission type.
   - **Reducer:** Count occurrences of each admission type per hospital.

7. **Gender-wise Frequency of Medical Conditions**
   - **Mapper:** Emit gender and medical condition.
   - **Reducer:** Count condition frequency for each gender.

8. **Average Test Result Distribution per Doctor**
   - **Mapper:** Emit doctor name and test result.
   - **Reducer:** Calculate percentage of Normal, Abnormal, Inconclusive results per doctor.

9. **Most Frequently Used Hospital Rooms**
   - **Mapper:** Emit room number.
   - **Reducer:** Count how often each room was used.

10. **Billing Analysis Across Age Groups**
    - **Mapper:** Emit age group and billing amount.
    - **Reducer:** Calculate average billing per age group.

---

## 🛠️ Technologies Used

- Apache Hadoop (MapReduce)
- Java or Python
- HDFS for dataset storage and job execution
