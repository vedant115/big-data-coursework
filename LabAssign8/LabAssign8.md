# Lab Assignment 8

## 📘 Assignment Overview

This lab extends the graph-based analysis of the tuberculosis symptoms dataset by applying advanced graph algorithms. These operations deepen insights into symptom relationships, influence, and network structure.

---

## 🧠 Objectives

- Apply various graph analytics techniques to the tuberculosis symptoms graph.
- Extract meaningful patterns about symptom co-occurrence, influence, and community structure.
- Use graph visualization tools to better understand network dynamics.

---

## 📂 Dataset

- **Dataset:** Tuberculosis symptoms dataset (`Tb disease symptoms.csv`)  
- **Source:** Same as Lab Assignment 7  
- **Prerequisite:** Completed graph construction in Lab Assignment 7

---

## ⚙️ Graph Operations and Use Cases

1. **Triangle Count**  
   - Detect clusters of interconnected symptoms and diseases.  
   - Identify common co-occurring symptoms in tuberculosis.

2. **Strongly Connected Components (SCC)**  
   - Identify groups where every symptom/disease is reachable from any other in the same group.  
   - Analyze symptom progression and interdependencies.

3. **Betweenness Centrality**  
   - Measure how often a node appears on the shortest paths between other nodes.  
   - Identify critical symptoms bridging different clusters.

4. **Degree Distribution**  
   - Analyze the number of connections each node has.  
   - Distinguish rare vs. common symptoms based on connectivity.

5. **Closeness Centrality**  
   - Measure closeness of a node to all others in the graph.  
   - Identify symptoms appearing early in disease progression.

6. **Eigenvector Centrality**  
   - Rank influential nodes based on connections to other high-scoring nodes.  
   - Determine symptom influence within the disease network.

7. **Label Propagation Algorithm (LPA)**  
   - Detect communities by propagating labels across the network.  
   - Automatically group related symptoms and disease categories.

8. **Jaccard Similarity**  
   - Measure similarity between nodes based on shared neighbors.  
   - Identify frequently co-occurring symptoms.

9. **K-Core Decomposition**  
   - Find subsets where each node connects to at least "k" other nodes.  
   - Understand the core structure of the symptom network.

10. **Graph Visualization**  
    - Use tools like **Gephi** or **GraphFrames** for visualizing node connections and communities.  
    - Provide intuitive insights into symptom relationships.

---

## 🛠️ Technologies Used

- Apache Spark (GraphX, GraphFrames)
- Gephi (or equivalent graph visualization tools)
- Hadoop/HDFS for data storage

---