# quiz_generator_no_nltk.py
import os
import random
import spacy
from dotenv import load_dotenv
import openai

# load .env BEFORE using OPENAI key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise RuntimeError("OPENAI_API_KEY not found. Add it to .env or environment variables.")

# load spacy model (will raise if not installed)
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    raise RuntimeError(
        "SpaCy model 'en_core_web_sm' not installed. Run:\n"
        "python -m spacy download en_core_web_sm\n"
    )

def generate_contextual_quiz(text, num_questions=5):
    # Split text into sentences using spaCy
    doc = nlp(text)
    sents = list(doc.sents)
    random.shuffle(sents)
    
    quiz = []
    for sent in sents:
        target = None
        if sent.ents:
            target = sent.ents[0].text
        elif list(sent.noun_chunks):
            target = list(sent.noun_chunks)[0].text
        if target:
            question = str(sent).replace(target, "_____")
            quiz.append({"question": question, "answer": target, "context": str(sent)})
        if len(quiz) >= num_questions:
            break
    return quiz

if __name__ == "__main__":
    sample_text = "Albert Einstein was a famous physicist. He developed the theory of relativity."
    quiz = generate_contextual_quiz(sample_text, num_questions=3)
    for i, q in enumerate(quiz, 1):
        print(f"Q{i}: {q['question']} (Answer: {q['answer']})")
