# modules/gameplay_frosmore.py

import random
import pathlib
import re
from PyPDF2 import PdfReader

BASE_DIR = pathlib.Path("packets/Froshmore")

def get_question(difficulty: str = "medium") -> dict:
    files = list(BASE_DIR.glob("*.pdf"))
    if not files:
        return {"text": "No Froshmore packets available.", "answer": ""}

    chosen_file = random.choice(files)
    questions = _load_pdf(chosen_file)

    for q in questions:
        if "difficulty" not in q:
            q["difficulty"] = _assign_difficulty(q["text"])

    filtered = [q for q in questions if q["difficulty"] == difficulty]
    return random.choice(filtered or questions)

def _load_pdf(path: pathlib.Path) -> list[dict]:
    reader = PdfReader(str(path))
    text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    blocks = re.findall(r"\d+\.\s*(.*?)\nANSWER:\s*(.*?)\n", text, re.DOTALL)
    return [{"text": q.strip(), "answer": a.strip()} for q, a in blocks]

def _assign_difficulty(text: str) -> str:
    text_lower = text.lower()
    if any(term in text_lower for term in ["obscure", "theorem", "19th century"]):
        return "hard"
    elif any(term in text_lower for term in ["capital", "president", "basic"]):
        return "easy"
    return "medium"