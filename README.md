🚀 Resume Analyzer

A simple Resume Analyzer web application that compares a resume with a job description and provides a match score, missing skills, and improvement suggestions using traditional Natural Language Processing techniques like TF-IDF and Cosine Similarity.

📌 Features

📄 Upload Resume (PDF format)
📝 Paste Job Description
📊 Match Score using TF-IDF + Cosine Similarity
❌ Missing Skills Detection
💡 Basic improvement suggestions
⚡ Simple and interactive Streamlit UI

🧠 How It Works

Extracts text from uploaded resume (PDF)
Preprocesses and cleans the text
Converts text into numerical vectors using TF-IDF Vectorization
Computes similarity using Cosine Similarity
Compares resume with job description
Identifies missing keywords/skills

🛠️ Tech Stack

Python 🐍
Streamlit 📊
Scikit-learn (TF-IDF, Cosine Similarity)
pdfplumber / PyPDF2 📄
NLP (Text Processing)

📊 Output

Match Score (0–100%)
List of missing skills
Basic improvement tips

💼 Use Cases

Students checking resume quality
Job seekers improving CVs
Basic ATS-style resume screening demo
NLP learning project

🔥 Future Improvements

Better skill extraction model
Multiple resume comparison
Job role categorization
Advanced scoring system
Resume keyword optimization
