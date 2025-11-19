# modules/adaptive_engine.py

import random

def adjust_difficulty(current_difficulty: str, correct: bool) -> str:
    levels = ["easy", "medium", "hard"]
    index = levels.index(current_difficulty)

    if correct and index < 2:
        return levels[index + 1]
    elif not correct and index > 0:
        return levels[index - 1]
    return current_difficulty

def select_question(questions: list[dict], difficulty: str) -> dict:
    filtered = [q for q in questions if q.get("difficulty") == difficulty]
    return random.choice(filtered or questions)