import sys
import os

# ✅ path fix
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
from Backend.main import extract_text, clean_text, get_similarity, get_missing_skills, get_suggestions

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("🚀 AI Resume Analyzer")

resume_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("📝 Paste Job Description")

if st.button("Analyze"):
    if resume_file and job_desc:
        
        # Extract
        resume_text = extract_text(resume_file)

        # Clean
        clean_resume = clean_text(resume_text)
        clean_jd = clean_text(job_desc)

        # Similarity
        score = get_similarity(clean_resume, clean_jd)

        # Skills
        missing = get_missing_skills(clean_resume, clean_jd)
        suggestion = get_suggestions(score)

        # ---------------- UI ----------------
        st.subheader("📊 Result")

        st.metric("Match Score", f"{score:.2f}%")
        st.progress(int(score))

        # Skills
        st.subheader("❌ Missing Skills")
        if missing:
            st.write(", ".join(missing))
        else:
            st.success("No major skills missing 🎉")

        # Suggestions
        st.subheader("💡 Suggestions")
        st.info(suggestion)

    else:
        st.warning("Please upload resume and paste job description")