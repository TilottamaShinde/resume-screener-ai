import re
import string

def clean_text(text):

    """
    Clean the input text by:
    - lowercasing
    - removing punctuations
    - removing extra spaces
    """
    text = text.lower()
    text = text.translate(str.maketrans('','',string.punctuation))
    text = re.sub(r'\s+',' ', text)
    return text.strip()

def extract_keyword(text):
    """
    Extract keywords from text by splitting on spaces and removing short/common words
    :param text:
    :return:
    """

    stop_words = set([
        'and', 'or', 'the', 'a', 'an', 'in', 'on', 'with', 'for', 'to', 'of',
        'is', 'are', 'was', 'were', 'this', 'that', 'it'
    ])
    words = clean_text(text).split()
    keywords = [word for word in words if word not in stop_words and len(word) > 2]
    return keywords