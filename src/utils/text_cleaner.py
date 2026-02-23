import re
import nltk
from nltk.corpus import stopwords

# Ensure stopwords are available
try:
    stop_words = set(stopwords.words("english"))
except:
    nltk.download("stopwords")
    stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = str(text)

    text = re.sub(r'^.*?\([\w\s]+\)\s*[-—]\s*', '', text)

    # Standard cleaning
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)
