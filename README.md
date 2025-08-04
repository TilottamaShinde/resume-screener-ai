# 📄 Resume Screener AI

An AI-powered Python project to automatically screen and score resumes based on job descriptions. This tool helps recruiters and hiring teams quickly identify the most relevant resumes from a pool of applicants.

---

## 🔍 Features

- Extracts text from PDF resumes
- Matches resume content with job description keywords
- Ranks resumes based on keyword match score
- Exports results to a CSV file
- Easy to customize and extend

---

## 🗂 Project Structure

resume_screener_ai/

├──  # Folder to place all the PDF resumes

├── job_description.txt # Paste the job description here

├── screener.py # Main script to run

├── export_results.py # Exports results to CSV

├── 

│ └── parse_resume.py # PDF text extraction logic




---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/resume-screener-ai.git
cd resume-screener-ai
```

├── screening_results.csv # Output file with results

├── requirements.txt # Dependencies list

└── README.md # Project documentation

python3 -m venv .venv

source .venv/bin/activate  # On macOS/Linux

# .venv\Scripts\activate   # On Windows

pip install -r requirements.txt


## Future Improvements

Add Streamlit web UI

Visualize match scores

Integrate with email/job portals

NLP-powered keyword suggestions
