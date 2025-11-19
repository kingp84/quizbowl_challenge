# modules/security.py

def sanitize_input(text: str) -> str:
    return text.replace("'", "").replace(";", "")