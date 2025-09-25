from conversions import (
    get_cad_to_usd_rate,
    get_clp_to_usd_rate,
)

# manual expenses
manual_expenses = [
    ("USD", 120),
    ("CAD", 80),
    ("CLP", 50000),
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
PREVIOUS_AMOUNT_USD = sum(convert_to_usd(amount, currency) for currency, amount in manual_expenses)