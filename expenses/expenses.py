import pandas as pd
from conversions import get_usd_to_clp_rate

file_name = "Saldo_y_Mov_No_Facturado.xls"
df = pd.read_excel(file_name, header=17)
df = df.dropna(axis=1, how="all")
df = df.dropna(how="all")
df = df.reset_index(drop=True)

rate_usd_clp = get_usd_to_clp_rate()
print(f"USD → CLP rate: {rate_usd_clp}")

# sum the “Monto (USD)” column
# make sure to drop or ignore NaNs; convert dtype if it's string etc.
usd_sum = df["Monto (USD)"].dropna().astype(float).sum()
print(f"Total USD amount: {usd_sum}")

# convert to CLP
total_clp = usd_sum * rate_usd_clp
print(f"Total in CLP: {total_clp:.2f}")