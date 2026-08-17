# Car Recommendation System (Vector Similarity Search)

> **A Practice Learning Project Exploring Feature Engineering, Vector Search (FAISS), and Data Product Delivery**

---

## 📌 Project Overview

This repository is an interactive recommendation tool built with **Python**, **FAISS (Facebook AI Similarity Search)**, and **Streamlit**. 

Traditional recommendation tools rely solely on rigid database queries (e.g., `WHERE price <= X AND fuel = Y`). This project demonstrates how to combine **hard constraint filtering** with **multidimensional similarity scoring (Vector Search)** to rank and recommend relevant vehicles based on normalized numeric feature vectors.

---

## 🎯 Relevance

As the boundaries between classic data analysis, business intelligence, and ML operations blur, modern data analysts are increasingly expected to understand **recommendation algorithms, vector embeddings, and feature engineering**. 

Here is how this project maps directly to core Data Analytics competencies:

| Data Analyst Competency | How it's Applied in this Project |
| :--- | :--- |
| **1. Data Engineering & Sanitization** | Handling missing attributes safely (e.g., missing price points, missing cylinder counts for Electric Vehicles) to prevent model pipeline crashes. |
| **2. Feature Scaling & Normalization** | Transforming raw multi-type data (categorical strings, integer cylinders, price ranges) into normalized numeric arrays suitable for mathematical distance calculation. |
| **3. Multi-Stage Filtering Pipelines** | Building a two-tier pipeline: Tier 1 filters out non-qualifying records (hard price & brand caps), while Tier 2 ranks qualifying options using similarity metrics. |
| **4. Vector Similarity Search (FAISS)** | Implementing $L_2$ Euclidean distance vectors using FAISS to measure item similarity in a 5-dimensional feature space. |
| **5. Business Intelligence & UI Delivery** | Building an interactive frontend using Streamlit to present algorithmic outputs directly to stakeholders in an accessible format. |

---

