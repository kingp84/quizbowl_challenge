import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# -----------------------------
# Square Settings
# -----------------------------
SQUARE_ACCESS_TOKEN = os.getenv("EAAAl__EnHnbvOhuduumqM6J5pDctA3rQPk6ejlVLkCe7TnSRBLkfIGdJ7NASfOR", "")
SQUARE_ENV = os.getenv("SQUARE_ENV", "production")  # "sandbox" or "production"
SQUARE_LOCATION_ID = os.getenv("L64NQWVTGM6RG", "")
SQUARE_WEBHOOK_SIGNATURE_KEY = os.getenv("0rHCQABw6WaCwQ0kqLYdNQ", "")

# -----------------------------
# Donation Endpoint
# -----------------------------
DONATION_ENDPOINT = os.getenv("DONATION_ENDPOINT", "https://www.myschoolbucks.com/ver2/prdembd?ref=ZZH510MFH9083MG_ZZ5YBXE762OW32S")

# -----------------------------
# Helper Functions
# -----------------------------
def is_configured() -> bool:
    """Quick check to ensure at least one provider is configured."""
    return any([
        SQUARE_ACCESS_TOKEN
    ])
