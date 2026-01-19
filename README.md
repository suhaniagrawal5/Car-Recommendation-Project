Car Recommendation System (API-Based)

📌 Overview
A car recommendation system built using external public APIs, FAISS vector similarity search, and Streamlit.
This project does not use any LLM and generates recommendations using feature-based similarity matching.

🎯 Features
Fetches real car models using a public API
Recommends cars based on user preferences
Uses FAISS for fast similarity search
Lightweight, explainable, and cost-free

🧠 How It Works
Fetch car data from an external API
Convert car attributes into numeric vectors
Store vectors in FAISS index
Convert user input into a query vector
Retrieve top matching cars

🛠️ Tech Stack
Python
Streamlit
FAISS
Public Vehicle API

⚙️ How to Run
streamlit run app.py
