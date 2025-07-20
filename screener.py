import os
from src.parse_resume import extract_text_from_pdf
from src.vectorizer import get_tfidf_similarity, get_semantic_similarity, ADVANCED