import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

# ---------------------------
# NAV HISTORY
# ---------------------------

nav = pd.read_csv("data/raw/datasets/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

print("NAV cleaned")


# ---------------------------
# INVESTOR TRANSACTIONS
# ---------------------------

txn = pd.read_csv(
    "data/raw/datasets/08_investor_transactions.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.title()
)

txn = txn[
    txn["transaction_type"].isin(
        ["Sip", "Lumpsum", "Redemption"]
    )
]

txn = txn[
    txn["amount_inr"] > 0
]

txn.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("Transactions cleaned")


# ---------------------------
# SCHEME PERFORMANCE
# ---------------------------

perf = pd.read_csv(
    "data/raw/datasets/07_scheme_performance.csv"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

perf["expense_ratio_flag"] = (
    (perf["expense_ratio_pct"] < 0.1)
    |
    (perf["expense_ratio_pct"] > 2.5)
)

perf.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("Performance cleaned")