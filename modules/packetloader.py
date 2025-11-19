# modules/packetloader.py

def get_question(format: str, difficulty: str = "medium") -> dict:
    from modules.hybrid_loader import get_hybrid_question
    return get_hybrid_question(format, difficulty)

