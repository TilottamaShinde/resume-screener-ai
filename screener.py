import os
from parse_resume import extract_text_from_pdf
from vectorizer import get_tfidf_similarity, get_semantic_similarity, ADVANCED

RESUMES_DIR = 'resumes'
JOB_DESC_FILE = 'job_description.txt'

def load_job_description(filepath: str) -> str:
    """Read job description from file"""
    with open(filepath, 'r', encoding = 'utf-8') as f:
        return f.read()

def screen_resumes():
    if not os.path.exists(RESUMES_DIR):
        print(f"Resume folder '{RESUMES_DIR}' not found")
        return

    try:
        jd_text = load_job_description(JOB_DESC_FILE)
    except FileNotFoundError:
        print(f"Job description file '{JOB_DESC_FILE}' not found.")
        return

    results = []

    for filename in os.listdir(RESUMES_DIR):
        if filepath.endswith('.pdf'):
            path = os.path.join(RESUMES_DIR, filename)
            try:
                resume_text = extract_text_from_pdf(path)
                if ADVANCED:
                    score = get_semantic_similarity(resume_text, jd_text)
                else:
                    score = get_tfidf_similarity(resume_text, jd_text)
                results.append((filename, score))
                print(f"Scored {filename} -> {score}")
            except Exception as e:
                print(f"Failed to process {filename}:{e}")

    results.sort(key = lambda x: x[1], reverse = True)

    print("\n Top Matching Resumes:")
    for i, (name, score) in enumerate(results, 1):
        print(f"{i}. {name} - Score:{score}")

if __name__ == "__main__":
    screen_resumes()
