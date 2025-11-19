# modules/hybrid_loader.py

from modules.packetloader_naqt import get_question as naqt
from modules.packetloader_ossaa import get_question as ossaa
from modules.gameplay_frosmore import get_question as froshmore

def get_hybrid_question(format: str, difficulty: str = "medium") -> dict:
    if format == "NAQT":
        return naqt(difficulty)
    elif format == "OSSAA":
        return ossaa(difficulty)
    elif format == "Froshmore":
        return froshmore(difficulty)
    return {"text": "Unknown format", "answer": ""}