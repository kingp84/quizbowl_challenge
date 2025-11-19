# modules/avatar.py

def get_avatar_url(name: str) -> str:
    # Placeholder avatar logic
    return f"https://api.dicebear.com/6.x/thumbs/svg?seed={name.replace(' ', '')}"