# expenses.py

import pandas as pd
import glob
import os
from conversions import get_usd_to_clp_rate
# from calculate_previous import PREVIOUS_AMOUNT_USD

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

# === Sum USD column safely (fix for non-numeric values like '1 / 0') ===
amount_col = "Unnamed: 10"

# Convert column to cleaned strings
s = df_all[amount_col].astype(str).str.strip()

# Optional: handle common Spanish/Chile number formatting:
# - thousands separator '.'  -> removed
# - decimal separator ','    -> replaced with '.'
s = s.str.replace(".", "", regex=False).str.replace(",", ".", regex=False)

# Convert to numeric; invalid parses become NaN instead of crashing
amount_num = pd.to_numeric(s, errors="coerce")

# Debug: show distinct bad values (non-empty) that couldn't be parsed
bad_mask = amount_num.isna() & s.ne("") & s.ne("nan") & s.ne("None")
if bad_mask.any():
    print("\nNon-numeric values found in 'Monto ($)' (these will be ignored):")
    print(df_all.loc[bad_mask, [amount_col]].drop_duplicates().to_string(index=False))

# Sum numeric values only
usd_sum = amount_num.dropna().sum()

# Add manual previous amount
usd_sum_total = usd_sum  # + PREVIOUS_AMOUNT_USD

print(f"Transactions from Excel files (USD): {usd_sum:.2f}")
# print(f"Previous manual expenses (USD): {PREVIOUS_AMOUNT_USD:.2f}")
print(f"Total USD amount: {usd_sum_total:.2f}")

# Convert to CLP
total_clp = usd_sum_total * rate_usd_clp
print(f"Total in CLP: {total_clp:.2f}")