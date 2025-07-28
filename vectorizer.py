from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

try:
    from sentence_transformers import SentenceTransformer
    ADVANCED = True
    model = SentenceTransformer('all-MiniLM-L6-v2')
except ImportError:
    ADVANCED = False
    model = None

def get_tfidf_similarity(resume_text: str, job_description: str) -> float:
    """
        Calculates cosine similarity between resume and job description using TF-IDF.

        Args:
            resume_text (str): Resume content as string.
            job_description (str): JD content as string.

        Returns:
            float: Similarity score between 0 and 1.
        """
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_description])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(score, 4)

def get_semantic_similarity(resume_text: str, job_description: str) -> float:
    """
        Calculates semantic similarity using sentence-transformers if available.

        Args:
            resume_text (str): Resume content.
            job_description (str): Job description content.

        Returns:
            float: Semantic similarity score.
        """
    if not ADVANCED:
        raise ImportError("SentenceTransformer is not installed. Run: pip install sentence-transformer")

    embeddings = model.encode([resume_text, job_description])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return round(score, 4)
