import pdfplumber
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------
# PDF TEXT EXTRACTION
# -----------------------------
def extract_text_from_pdf(pdf_file):

    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + " "

    # CLEAN TEXT
    text = text.replace("\n", " ")
    text = text.replace("\r", " ")

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip().lower()

# -----------------------------
# SKILL LIST
# -----------------------------
SKILL_SET = [

    "python",
    "sql",
    "machine learning",
    "deep learning",
    "streamlit",
    "fastapi",
    "flask",
    "docker",
    "git",
    "github",
    "pandas",
    "numpy",
    "scikit learn",
    "scikit-learn",
    "tensorflow",
    "keras",
    "nlp",
    "natural language processing",
    "data analysis",
    "power bi",
    "excel"

]



# -----------------------------
# EXTRACT SKILLS
# -----------------------------
def extract_skills(text):
    if not text:
        return []

    text = text.lower().replace("-", " ")
    found_skills = []

    for skill in SKILL_SET:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.append(skill)

    # OPTIONAL: also capture unknown keywords (simple fallback)
    words = set(text.split())
    for word in words:
        if len(word) > 2 and word not in found_skills:
            if word in ["ai", "ml", "dl"]:
                found_skills.append(word)

    return list(set(found_skills))


# -----------------------------
# MATCH SCORE
# -----------------------------
def calculate_match_score(resume_text, job_description):

    if not resume_text or not job_description:
        return 0.0

    documents = [resume_text, job_description]

    tfidf = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)  # ⭐ IMPORTANT IMPROVEMENT
    )

    matrix = tfidf.fit_transform(documents)

    similarity = cosine_similarity(matrix[0:1], matrix[1:2])

    return round(float(similarity[0][0]) * 100, 2)

def calculate_skill_score(resume_skills, job_description):

    if not job_description:
        return 0.0

    job_skills = extract_skills(job_description)

    if not job_skills:
        return 0.0

    matched = len(set(resume_skills).intersection(set(job_skills)))
    total = len(set(job_skills))

    return (matched / total) * 100 if total > 0 else 0

def calculate_final_score(resume_text, job_description, resume_skills):

    tfidf_score = calculate_match_score(resume_text, job_description)
    skill_score = calculate_skill_score(resume_skills, job_description)

    tfidf_score = min(tfidf_score, 100)
    skill_score = min(skill_score, 100)

    final_score = (0.6 * tfidf_score) + (0.4 * skill_score)

    return round(final_score, 2), tfidf_score, skill_score    



# -----------------------------
# MATCH LEVEL
# -----------------------------
def get_match_level(score):

    if score >= 70:
        return "✅ Strong Match"

    elif score >= 40:
        return "⚠️ Moderate Match"

    else:
        return "❌ Weak Match"




# -----------------------------
# MISSING SKILLS
# -----------------------------
def get_missing_skills(resume_text, job_description):

    resume_skills = set(
        extract_skills(resume_text)
    )

    job_skills = set(
        extract_skills(job_description)
    )


    return list(job_skills.difference(resume_skills))


# -----------------------------
# SKILL IMPORTANCE SYSTEM
# -----------------------------
def classify_skill_importance(skills):

    high_priority = [
        "python",
        "machine learning",
        "sql"
    ]

    medium_priority = [
        "streamlit",
        "fastapi",
        "git",
        "github",
        "pandas",
        "numpy",
        "data analysis",
        "power bi"
    ]

    low_priority = [
        "docker"
    ]

    result = {
        "High Priority": [],
        "Medium Priority": [],
        "Low Priority": []
    }

    for skill in skills:

        skill = skill.lower()

        if skill in high_priority:
            result["High Priority"].append(skill)

        elif skill in medium_priority:
            result["Medium Priority"].append(skill)

        elif skill in low_priority:
            result["Low Priority"].append(skill)

    return result

# -----------------------------
# AI FEEDBACK GENERATOR (ADD HERE)
# -----------------------------
def generate_feedback(resume_text, job_text, missing_skills, match_score):

    feedback = []

    # Overall score feedback
    if match_score > 80:
        feedback.append("Excellent match! Your resume is highly aligned with the job description.")
    elif match_score > 60:
        feedback.append("Good match, but there is room for improvement in key technical skills.")
    else:
        feedback.append("Low match. You should improve both skills and project alignment.")

    # Missing skills feedback
    if missing_skills:
        feedback.append("\nKey Missing Skills:")
        for skill in missing_skills:
            feedback.append(f"- Add {skill}: It is commonly required in this role.")

    # Resume quality checks
    if "project" not in resume_text.lower():
        feedback.append("\nAdd more projects to strengthen your profile.")

    if "github" not in resume_text.lower():
        feedback.append("Include GitHub profile to showcase your work.")

    if len(resume_text.split()) < 200:
        feedback.append("Your resume looks short. Add more details about skills and projects.")

    return "\n".join(feedback)

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile

def generate_pdf_report(
    score,
    match_level,
    recommendation,
    matched_skills,
    missing_skills,
    high_priority,
    medium_priority,
    low_priority
):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

    pdf = canvas.Canvas(temp_file.name, pagesize=letter)

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, 750, "Resume Analysis Report")

    pdf.setFont("Helvetica", 12)

    y = 710

    pdf.drawString(50, y, f"Match Score: {score:.2f}%")
    y -= 20

    pdf.drawString(50, y, f"Match Level: {match_level}")
    y -= 20

    pdf.drawString(50, y, f"Recommendation: {recommendation}")
    y -= 40

    pdf.drawString(50, y, "Matched Skills:")
    y -= 20
    pdf.drawString(70, y, ", ".join(matched_skills))
    y -= 40

    pdf.drawString(50, y, "Missing Skills:")
    y -= 20
    pdf.drawString(70, y, ", ".join(missing_skills) if missing_skills else "None")

    pdf.save()

    return temp_file.name