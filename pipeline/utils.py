import os

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def save_text(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
