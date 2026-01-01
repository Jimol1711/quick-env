# expenses.py

import pandas as pd
import glob
import os
from conversions import get_usd_to_clp_rate
from calculate_previous import PREVIOUS_AMOUNT_USD

# === Helper to load a single file ===
def load_statement(file_path):
    df = pd.read_excel(file_path, header=17)
    df = df.dropna(axis=1, how="all")
    df = df.dropna(how="all")
    df = df.reset_index(drop=True)
    return df

# === Load the base file ===
base_file = "Saldo_y_Mov_No_Facturado.xls"
df_base = load_statement(base_file)

# === Load all files inside new/ ===
new_files = glob.glob(os.path.join("new", "*.xls"))
df_new_list = [load_statement(f) for f in new_files]

# === Merge all into one DataFrame ===
df_all = pd.concat([df_base] + df_new_list, ignore_index=True)

# === Drop exact duplicates (row-wise) ===
df_all = df_all.drop_duplicates()

# === Reset index after cleanup ===
df_all = df_all.reset_index(drop=True)

# === Conversion ===
rate_usd_clp = get_usd_to_clp_rate()
print(f"USD → CLP rate: {rate_usd_clp}")

# Sum USD column
usd_sum = df_all["Monto (USD)"].dropna().astype(float).sum()

# Add manual previous amount
usd_sum_total = usd_sum + PREVIOUS_AMOUNT_USD

print(f"Transactions from Excel files (CLP): {usd_sum:.2f}")
print(f"Previous manual expenses (CLP): {PREVIOUS_AMOUNT_USD:.2f}")
print(f"Total CLP amount: {usd_sum_total:.2f}")

# Convert to CLP
total_clp = usd_sum_total * rate_usd_clp
print(f"Total in CLP: {total_clp:.2f}")