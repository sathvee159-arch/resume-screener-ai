import streamlit as st
from utils import generate_pdf_report
from utils import generate_feedback
from utils import (
    extract_text_from_pdf,
    calculate_final_score,
    get_match_level,
    extract_skills,
    get_missing_skills,
    classify_skill_importance
)

st.set_page_config(page_title="Resume Screener AI")

st.title("📄 Resume Screener AI")

uploaded_resumes = st.file_uploader(
    "Upload Resumes (PDF)",
    type=["pdf"],
    accept_multiple_files=True
)

job_description = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze Resume"):

    if uploaded_resumes and job_description:
        results=[]
        for uploaded_resume in uploaded_resumes:

            # -----------------------------
            # EXTRACT TEXT
            # -----------------------------
            resume_text = extract_text_from_pdf(uploaded_resume)

            # -----------------------------
            # SKILL ANALYSIS
            # -----------------------------
            resume_skills = extract_skills(resume_text)
            missing_skills = get_missing_skills(resume_text, job_description)
            skill_importance = classify_skill_importance(resume_skills)

            # -----------------------------
            # MATCH SCORE
            # -----------------------------
            score, tfidf_score, skill_score = calculate_final_score(
                resume_text,job_description,resume_skills)

            level = get_match_level(score)

            # STORE ONLY 
            results.append({
                "name": uploaded_resume.name,
                "score": score,
                "tfidf": tfidf_score,
                "skill": skill_score,
                "level": level,
                "resume_text": resume_text,
                "resume_skills": resume_skills,
                "missing_skills": missing_skills,
                "skill_importance": skill_importance
            })
        results = sorted(results, key=lambda x: x["score"], reverse=True)

        # -----------------------------
        # 🏆 RANKING UI
        # -----------------------------
        st.subheader("📊 Detailed Resume Analysis")

        for res in results:

            st.markdown(f"## 📄 {res['name']}")

            st.write(f"Final ATS Score: {res['score']:.2f}%")
            st.write(f"TF-IDF Score: {res['tfidf']:.2f}%")
            st.write(f"Skill Score: {res['skill']:.2f}%")

            st.progress(min(int(res["score"]), 100))
            st.write(res["level"])

            feedback = generate_feedback(
                res["resume_text"],
                job_description,
                res["missing_skills"],
                res["score"]
            )

            st.subheader("🧠 AI Feedback Suggestions")
            st.text_area("Feedback", feedback, height=150)

            st.subheader("🎯 Skill Importance")
            st.write("🟢 High Priority")
            st.write(", ".join(res["skill_importance"]["High Priority"]) or "None")

            st.write("🟡 Medium Priority")
            st.write(", ".join(res["skill_importance"]["Medium Priority"]) or "None")

            st.write("🔴 Low Priority")
            st.write(", ".join(res["skill_importance"]["Low Priority"]) or "None")

            st.subheader("✅ Matched Skills")
            st.write(", ".join(res["resume_skills"]) or "None")

            st.subheader("❌ Missing Skills")
            st.write(", ".join(res["missing_skills"]) or "None")

            pdf_path = generate_pdf_report(
                res["score"],
                res["level"],
                "Good match analysis completed",
                res["resume_skills"],
                res["missing_skills"],
                res["skill_importance"]["High Priority"],
                res["skill_importance"]["Medium Priority"],
                res["skill_importance"]["Low Priority"]
            )

            with open(pdf_path, "rb") as pdf_file:
                st.download_button(
                    label=f"📄 Download Report - {res['name']}",
                    data=pdf_file,
                    file_name=f"{res['name']}_report.pdf",
                    mime="application/pdf"
                )

            st.markdown("---")

    else:
        st.warning("Please upload resumes and enter job description.")