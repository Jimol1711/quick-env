from conversions import (
    get_cad_to_usd_rate,
    get_clp_to_usd_rate,
)

# manual expenses
manual_expenses = [
    ("CAD", 50),
    ("CAD", 160),
    ("CAD", 1100),
    ("CAD", 7),
    ("USD", 21),
    ("CLP", 12000),
    ("USD", 2200),
    ("CAD", 348.95),
    ("CLP", 78000),
    ("CAD", 187.2),
    ("CLP", 50000)
]

def convert_to_usd(amount, currency):
    """Convert a given amount in [USD, CAD, CLP] to USD."""
    if currency == "USD":
        return amount
    elif currency == "CAD":
        rate = get_cad_to_usd_rate()
        return amount * rate
    elif currency == "CLP":
        rate = get_clp_to_usd_rate()
        return amount * rate
    else:
        raise ValueError(f"Unsupported currency: {currency}")

# previous amount calculation
# PREVIOUS_AMOUNT_USD = sum(convert_to_usd(amount, currency) for currency, amount in manual_expenses)
# print(f"Previous amount in USD: {PREVIOUS_AMOUNT_USD:.2f}")