# Car Recommendation System

A lightweight practice project demonstrating how to build a recommendation engine using **FAISS vector search**, **feature engineering**, and **Streamlit**.

---

## 📌 Project Overview

This app combines **hard constraint filtering** (budget & brand) with **soft similarity scoring** (vector search) to recommend vehicles matching user preferences.

* **Frontend:** Streamlit interactive dashboard
* **Search Engine:** Meta's FAISS (L2 Euclidean Distance)
* **Dataset:** Local structured Python data dictionary (No API keys required)

---

## 📁 Repository Structure

| File | Description |
| :--- | :--- |
| `app.py` | Main Streamlit interface and recommendation workflow |
| `car_data.py` | Data provider layer & budget filtering logic |
| `vector_store.py` | Feature scaling and FAISS vector index builder |

---

## ⚡ Quickstart

### 1. Install Dependencies and Run program
```bash
pip install streamlit numpy faiss-cpu
streamlit run app.py
