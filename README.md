# 🧠 Resume-Based Course Recommender System

This is a **Django-based web application** that intelligently recommends Udemy courses by analyzing the contents of your uploaded resume. It utilizes **NLP embeddings** to match your resume to relevant course titles.

---

## 🚀 Features

- 📄 Upload a resume (`PDF` or `TXT`)
- 📚 Upload a dataset of Udemy courses (`CSV`)
- 🤖 Auto-recommend top-N most relevant courses
- ⚡ Fast, accurate semantic matching via `sentence-transformers`
- 🔍 Uses cosine similarity between embeddings for recommendation

---

## 🛠️ Tech Stack

| Layer        | Tech Used                                     |
|--------------|-----------------------------------------------|
| Backend      | Django, Python                                |
| NLP Model    | `sentence-transformers` (`distilbert-base-nli-mean-tokens`) |
| Data Format  | Custom `udemy_courses.csv` (title, link, price) |
| PDF Parsing  | `pdfplumber`                                  |
| Embeddings   | PyTorch tensor embeddings                     |
| Similarity   | Cosine similarity for ranking                 |

---

## 📊 System Architecture

graph TD
    A[User Uploads Resume (PDF/TXT)] --> B[Parse Text using pdfplumber or plain read]
    B --> C[Generate Sentence Embedding using DistilBERT]
    D[Upload Udemy CSV Dataset] --> E[Extract Course Titles]
    E --> F[Generate Embeddings for Courses]
    C --> G[Compare with Course Embeddings using Cosine Similarity]
    F --> G
    G --> H[Sort by Similarity Score]
    H --> I[Top N Course Recommendations]

---

## 📁 Folder Structure

graph TD
A[User Uploads Resume (PDF/TXT)] --> B[Parse Text using pdfplumber or plain r
ad] B --> C[Generate Sentence Embedding using Dis
ilBERT] D[Upload Udemy CSV Dataset] --> E[Extract Co
rse Titles] E --> F[Generate Embeddi
gs for Courses] C --> G[Compare with Course Embeddings usin
Cosine
Similarity] F --> G G -->
---

## 🧪 How It Works

1. **Resume Upload**: User uploads a resume in `.pdf` or `.txt` format.

2. **Text Extraction**: Resume is parsed to extract raw text using `pdfplumber`.

3. **Embedding Generation**:
   - Resume text is embedded using `sentence-transformers`.
   - Course titles from CSV are also embedded.

4. **Similarity Comparison**: Cosine similarity scores are calculated.

5. **Recommendation Output**: Top-N matching courses are displayed based on similarity scores.

---

## 🔧 Installation & Setup

1. **Clone the repository**
git clone https://github.com/dhruv-lakhe/course-recommender
cd resume_recommender

2. **Create virtual environment**
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**
pip install -r requirements.txt

4. **Run migrations**
python manage.py migrate

5. **Start development server**
python manage.py runserver

---

## 📦 Requirements

pip install -r requirements.txt

Key packages:
- Django
- pdfplumber
- sentence-transformers
- torch
- pandas

---

## 📖 Usage

1. Navigate to `http://localhost:8000`
2. Upload your resume (PDF/TXT format)
3. Upload Udemy courses dataset (CSV format)
4. Click "Get Recommendations"
5. View your personalized course suggestions!

---

## 📋 Dataset Format

Your Udemy courses CSV should have these columns:
title,link,price
"Python for Data Science","https://udemy.com/course/...",49.99
"Web Development Bootcamp","https://udemy.com/course/...",89.99

---

## ⚠️ Note

There is no live deployment currently — run locally using Django's development server.

---

## 🧠 Future Enhancements

- [ ] UI improvement with Tailwind or Bootstrap
- [ ] Add support for DOCX resumes
- [ ] Auto-fetch courses from Udemy API
- [ ] Live deployment on Vercel / Render / Railway

---

## 🤝 Acknowledgements

- [SentenceTransformers](https://www.sbert.net/)
- [Udemy](https://www.udemy.com/)
- [pdfplumber](https://github.com/jsvine/pdfplumber)

---

## 📬 Contact

Feel free to connect on LinkedIn or email at dhruvlakhe@gmail.com.
