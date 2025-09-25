import requests

def get_usd_to_clp_rate():
    """Return how many Chilean Pesos (CLP) per 1 USD."""
    url = "https://open.er-api.com/v6/latest/USD"
    resp = requests.get(url)
    data = resp.json()
    rate = data["rates"]["CLP"]
    return rate

def get_usd_to_cad_rate():
    """Return how many Canadian Dollars (CAD) per 1 USD."""
    url = "https://open.er-api.com/v6/latest/USD"
    resp = requests.get(url)
    data = resp.json()
    rate = data["rates"]["CAD"]
    return rate

def get_cad_to_usd_rate():
    """Return how many US Dollars per 1 CAD."""
    rate_usd_to_cad = get_usd_to_cad_rate()
    rate = 1.0 / rate_usd_to_cad
    return rate

def get_clp_to_usd_rate():
    """Return how many US Dollars per 1 Chilean Peso (CLP)."""
    rate_usd_to_clp = get_usd_to_clp_rate()
    rate = 1.0 / rate_usd_to_clp
    return rate

def get_cad_to_clp_rate():
    """Return how many Chilean Pesos per 1 Canadian Dollar."""
    usd_to_clp = get_usd_to_clp_rate()
    usd_to_cad = get_usd_to_cad_rate()
    cad_to_usd = 1.0 / usd_to_cad
    result = cad_to_usd * usd_to_clp
    return result

def get_clp_to_cad_rate():
    """Return how many Canadian Dollars per 1 Chilean Peso."""
    cad_to_clp = get_cad_to_clp_rate()
    rate = 1.0 / cad_to_clp
    return rate

# just to verify the conversions
if __name__ == "__main__":
    print("=== Conversion tests ===")

    # USD <-> CLP
    usd_to_clp = get_usd_to_clp_rate()
    clp_to_usd = get_clp_to_usd_rate()
    print(f"1 USD = {usd_to_clp:.2f} CLP")
    # print(f"1 CLP = {clp_to_usd:.6f} USD")

    # USD <-> CAD
    usd_to_cad = get_usd_to_cad_rate()
    cad_to_usd = get_cad_to_usd_rate()
    print(f"1 USD = {usd_to_cad:.4f} CAD")
    print(f"1 CAD = {cad_to_usd:.4f} USD")

    # CLP <-> CAD
    cad_to_clp = get_cad_to_clp_rate()
    clp_to_cad = get_clp_to_cad_rate()
    print(f"1 CAD = {cad_to_clp:.2f} CLP")
    # print(f"1 CLP = {clp_to_cad:.6f} CAD")