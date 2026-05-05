print("Backend loaded")

import pdfplumber
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------
# 📄 Extract text
# -------------------------------
def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


# -------------------------------
# 🧹 Clean text
# -------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


# -------------------------------
# 📊 Similarity (IMPROVED)
# -------------------------------
def get_similarity(resume, jd):
    tfidf = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
    vectors = tfidf.fit_transform([resume, jd])

    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return score * 100


# -------------------------------
# 🧠 Skill Matching (SMART)
# -------------------------------
SKILLS = [
    "python", "java", "c++", "sql", "mongodb",
    "machine learning", "ml", "deep learning",
    "data science", "data analysis",
    "pandas", "numpy", "matplotlib",
    "html", "css", "javascript", "react",
    "nodejs", "express",
    "docker", "kubernetes", "aws", "git",
    "flask", "django", "rest api"
]

def get_missing_skills(resume, jd):
    resume = resume.lower()
    jd = jd.lower()

    missing = []

    for skill in SKILLS:
        if skill in jd and skill not in resume:
            missing.append(skill)

    return missing


# -------------------------------
# 💡 Suggestions
# -------------------------------
def get_suggestions(score):
    if score > 80:
        return "Great match! Add measurable achievements and improve formatting."
    elif score > 60:
        return "Good match. Add more relevant skills and strong projects."
    else:
        return "Low match. Focus on required skills, projects, and keywords."