import pandas as pd
import requests

file_name = "Saldo_y_Mov_No_Facturado.xls"
df = pd.read_excel(file_name, header=17)
print(df)
df = df.dropna(axis=1, how="all")
df = df.dropna(how="all")
df = df.reset_index(drop=True)

df['Monto (USD)'].sum()

def get_usd_to_clp_rate():
    # Using ExchangeRate-API open endpoint
    url = "https://open.er-api.com/v6/latest/USD"
    resp = requests.get(url)
    data = resp.json()
    # The JSON has a "rates" object, with "CLP" inside
    rate = data["rates"]["CLP"]
    return rate

rate_usd_clp = get_usd_to_clp_rate()
print(f"USD → CLP rate: {rate_usd_clp}")

# 3. Sum the “Monto (USD)” column
#   Make sure to drop or ignore NaNs; convert dtype if it's string etc.
usd_sum = df["Monto (USD)"].dropna().astype(float).sum()
print(f"Total USD amount: {usd_sum}")

# 4. Convert to CLP
total_clp = usd_sum * rate_usd_clp
print(f"Total in CLP: {total_clp:.2f}")