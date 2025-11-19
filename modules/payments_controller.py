# modules/payments_controller.py

from modules.payments import calculate_total
from modules.payments_db import record_payment

def process_payment(user_id: int, cart: list[dict]) -> float:
    total = calculate_total(cart)
    record_payment(user_id, total)
    return total