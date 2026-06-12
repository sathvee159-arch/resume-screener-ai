# 📄 Resume Screener AI

An AI-powered Resume Screener web application built using **Python + Streamlit** that compares multiple PDF resumes against a job description and provides intelligent ATS scoring, ranking, and feedback.

---

## 🚀 Live Demo

👉 Resume Screener AI is deployed on Streamlit Cloud:

https://resume-screener-ai-a8aoxo6uqytreemmw9njux.streamlit.app/

---

## 🧠 Features

- 📤 Upload multiple PDF resumes
- 📄 Extract resume text using `pdfplumber`
- 🔍 Skill extraction using predefined skill list
- 📊 TF-IDF + Cosine Similarity for resume–JD matching
- 🧮 Skill-based scoring system
- 🎯 Final ATS Score (0–100)
  - 60% TF-IDF similarity score
  - 40% Skill matching score
- 📌 Match classification:
  - Strong Match
  - Moderate Match
  - Weak Match
- 🤖 AI-generated feedback suggestions
- ❌ Missing skill detection
- 📈 Skill importance classification (High / Medium / Low)
- 🏆 Resume ranking system
- 📥 Downloadable PDF analysis report using ReportLab

---

## ⚙️ Tech Stack

- Python
- Streamlit
- scikit-learn
- pdfplumber
- ReportLab
- Git & GitHub

---

## 📂 Project Structure

```text
resume-screener-ai/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── resume_parser.py
│   ├── scoring.py
│   └── feedback.py
│
├── assets/
│
└── sample_resumes/
```

---

## 🛠️ Installation & Run Locally

```bash
# Clone the repository
git clone https://github.com/sathvee159-arch/resume-screener-ai.git

# Move into project directory
cd resume-screener-ai

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

---

## 🌐 Deployment

This project is deployed using **Streamlit Cloud**.

Steps:

- Push project code to GitHub
- Connect repository with Streamlit Cloud
- Deploy the application

---

## 📊 How It Works

1. Upload multiple resumes in PDF format
2. Enter the job description
3. Extract text and skills from resumes
4. Compare resumes with job description using TF-IDF
5. Calculate skill matching score
6. Generate final ATS score
7. Rank resumes based on matching score
8. Provide feedback and improvement suggestions

---

## 📚 What I Learned

- Building web applications using Streamlit
- PDF text extraction using `pdfplumber`
- NLP concepts like TF-IDF and cosine similarity
- Resume matching and ATS scoring logic
- Git and GitHub workflow
- Deploying ML applications using Streamlit Cloud
- Building an end-to-end AI project

---

## 🏁 Future Improvements

- Multi-job comparison system
- Advanced NLP-based skill extraction (NER model)
- Resume improvement chatbot
- User authentication system
- Database integration for storing results
- More advanced AI-based resume recommendations

---

## 👨‍💻 Author

**Sathveeka M**  
B.Sc AI & ML Student  
Interested in Artificial Intelligence, Machine Learning, and Data Science
