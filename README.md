# 🧠 Resume-Based Course Recommender System

This project is a Django web application that recommends Udemy courses based on the contents of a user-uploaded resume. It uses **sentence embeddings** from `sentence-transformers` and compares them with course titles using **cosine similarity**.

---

## 🚀 Features

- Upload a resume (PDF or TXT)
- Upload a dataset of Udemy courses
- Auto-recommend top-N matching courses using NLP
- Torch-powered sentence similarity using `distilbert-base-nli-mean-tokens`

---

## 🛠️ Tech Stack

- **Backend:** Django, Python
- **NLP Model:** `sentence-transformers` (DistilBERT)
- **Data:** Custom `udemy_courses.csv` with course title, URL, and price
- **PDF Parsing:** `pdfplumber`
- **Embeddings Comparison:** PyTorch cosine similarity

---
