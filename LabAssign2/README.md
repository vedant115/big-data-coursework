# Lab Assignment 2

## 📘 Assignment Overview

This lab involves two key tasks: implementing matrix multiplication using Hadoop MapReduce and performing word count on a scraped web page using Python and Hadoop MapReduce.

---

## 🧠 Objectives

- Develop a Hadoop MapReduce program to perform matrix multiplication.
- Apply web scraping techniques and process the scraped data using a MapReduce-based word count.

---

## ⚙️ Task Details

### 1. Matrix Multiplication Using Hadoop MapReduce

- **Matrices:** A (3×3) and B (3×3), stored as text files in HDFS.
- **Mapper:**
  - Emit intermediate key-value pairs using composite indices.
- **Reducer:**
  - Compute the product of corresponding rows and columns.
  - Output individual elements of the resulting matrix.
- **Driver Program:**
  - Configure input and output paths.
  - Set job configurations for Mapper and Reducer classes.
- **Validation:**
  - Check the output matrix C against expected results for a 2×2 product.

### 2. Word Count on Scraped Wikipedia Page

- **Target Page:** [IIIT Allahabad Wikipedia Page](https://en.wikipedia.org/wiki/Indian_Institute_of_Information_Technology,_Allahabad)
- **Scraping Tool:** Use Python (e.g., `requests`, `BeautifulSoup`) to extract textual data.
- **Word Limit:** Truncate or filter to a maximum of **1500 words**.
- **MapReduce Implementation:**
  - Implement the word count in Java or Python using Hadoop.
  - Execute the job on the scraped content.
  - Share the word frequency output.

---

## 🛠️ Technologies Used

- Apache Hadoop (MapReduce)
- Java or Python
- Python libraries: `requests`, `BeautifulSoup` (for scraping)