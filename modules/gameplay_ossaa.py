# modules/gameplay_ossaa.py

from modules.packetloader_ossaa import get_question

def get_ossaa_question(difficulty: str = "medium") -> dict:
    return get_question(difficulty)