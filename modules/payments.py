# modules/payments.py

def calculate_total(cart: list[dict]) -> float:
    return sum(item["price"] for item in cart)