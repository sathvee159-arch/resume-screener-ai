# 📄 Resume Screener AI

An AI-powered Resume Screener web application built using **Python + Streamlit** that compares multiple PDF resumes against a job description and provides intelligent ATS scoring, ranking, and feedback.

---

## 🚀 Live Demo

👉 Resume Screener AI is deployed on Streamlit Cloud  
https://resume-screener-ai-a8aoxo6uqytreemmw9njux.streamlit.app/

---

## 🧠 Features

- 📤 Upload multiple PDF resumes
- 📄 Extract text using `pdfplumber`
- 🔍 Skill extraction using predefined skill list
- 📊 TF-IDF + Cosine Similarity for resume–JD matching
- 🧮 Skill-based scoring system
- 🎯 Final ATS Score (0–100)
  - 60% TF-IDF score
  - 40% skill score
- 📌 Match classification:
  - Strong Match
  - Moderate Match
  - Weak Match
- 🤖 AI-generated feedback suggestions
- ❌ Missing skill detection
- 📈 Skill importance classification (High / Medium / Low)
- 🏆 Resume ranking system
- 📥 Downloadable PDF report using ReportLab

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
resume-screener-ai/ │ ├── app.py ├── requirements.txt ├── README.md │ ├── utils/ │   ├── resume_parser.py │   ├── scoring.py │   ├── feedback.py │ ├── assets/ │ └── sample_resumes/

---

## 🛠️ Installation & Run Locally

```bash
# Clone the repository
git clone https://github.com/sathvee159-arch/resume-screener-ai.git

# Move into project directory
cd resume-screener-ai

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py

## 🌐 Deployment

This project is deployed using **Streamlit Cloud**:

- Push code to GitHub  
- Connect repository to Streamlit Cloud  
- Deploy with one click  

---

## 📊 How It Works

- Upload multiple resumes (PDF format)  
- Enter job description  
- System extracts skills and text  
- Computes TF-IDF similarity  
- Calculates skill match score  
- Generates final ATS score  
- Provides ranking and feedback  

---

## 📚 What I Learned

- Streamlit app development  
- PDF text extraction using `pdfplumber`  
- NLP basics (TF-IDF, cosine similarity)  
- Git & GitHub workflow  
- Deployment on Streamlit Cloud  
- Building end-to-end AI projects  

---

## 🏁 Future Improvements

- Multi-job comparison system  
- Advanced NLP skill extraction (NER model)  
- Resume improvement chatbot  
- Authentication system for users  
- Database integration (store resumes & results)  

---

## 👨‍💻 Author

**Sathveeka M**  
B.Sc AI & ML Student  
Passionate about AI, Data Science, and Web Development