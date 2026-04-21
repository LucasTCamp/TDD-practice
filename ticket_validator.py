def validate_ticket(code):
    if not isinstance(code, str):
        raise TypeError("code must be a string")
    if len(code) != 8:
        return False
    if not code.startswith("TK"):
        return False
    if not code[2:].isdigit():
        return False
    return True

def get_ticket_tier(code):
    if not validate_ticket(code):
        raise ValueError("invalid ticket code")
    digit = int(code[2])
    if digit <= 3:
        return "General"
    elif digit <= 6:
        return "VIP"
    else:
        return "Platinum"


def calculate_total(prices, discount=0):
    if not isinstance(prices, list):
        raise TypeError("prices must be a list")
    if len(prices) == 0:
        raise ValueError("prices cannot be empty")
    if discount < 0 or discount >= 1:
        raise ValueError("discount must be 0.0 to <1.0")
    return round(sum(prices) * (1 - discount), 2)