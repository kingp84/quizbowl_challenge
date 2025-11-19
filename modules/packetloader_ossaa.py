# modules/packetloader_ossaa.py

import json
import csv
import random
import pathlib
import re
from PyPDF2 import PdfReader

BASE_DIR = pathlib.Path("packets/OSSAA")

# --- Main entry point ---
def get_question(difficulty: str = "medium") -> dict:
    files = list(BASE_DIR.glob("*.*"))
    if not files:
        return {"text": "No NAQT packets available.", "answer": ""}

    chosen_file = random.choice(files)
    ext = chosen_file.suffix.lower()

    if ext == ".json":
        questions = _load_json(chosen_file)
    elif ext == ".csv":
        questions = _load_csv(chosen_file)
    elif ext == ".pdf":
        questions = _load_pdf(chosen_file)
    else:
        return {"text": f"Unsupported file type: {ext}", "answer": ""}

    # Preprocess with GPT-5 to assign difficulty
    for q in questions:
        if "difficulty" not in q or not q["difficulty"]:
            q["difficulty"] = _assign_difficulty(q["text"])

    filtered = [q for q in questions if q["difficulty"] == difficulty]
    return random.choice(filtered or questions)

# --- Loaders ---
def _load_json(path: pathlib.Path) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        packet = json.load(f)
    return packet.get("questions", [])

def _load_csv(path: pathlib.Path) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

def _load_pdf(path: pathlib.Path) -> list[dict]:
    reader = PdfReader(str(path))
    text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    blocks = re.findall(r"\d+\.\s*(.*?)\nANSWER:\s*(.*?)\n", text, re.DOTALL)
    questions = []
    for q_text, a_text in blocks:
        questions.append({
            "text": q_text.strip(),
            "answer": a_text.strip(),
            "difficulty": None  # Will be assigned later
        })
    return questions

# --- GPT-5 Difficulty Assigner (stub) ---
def _assign_difficulty(text: str) -> str:
    # Replace this stub with GPT-5 logic
    text_lower = text.lower()
    if any(hint in text_lower for hint in ["obscure", "theorem", "19th century", "philosopher", "molecular"]):
        return "hard"
    elif any(hint in text_lower for hint in ["capital", "president", "formula", "basic", "common"]):
        return "easy"
    else:
        return "medium"

