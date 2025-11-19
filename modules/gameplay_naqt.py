# modules/gameplay_naqt.py

from modules.packetloader_naqt import get_question

def get_naqt_question(difficulty: str = "medium") -> dict:
    return get_question(difficulty)