import pandas as pd
import os

raw_folder = "data/raw/datasets"
processed_folder = "data/processed"

files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    df = pd.read_csv(f"{raw_folder}/{file}")

    output_name = file.replace(".csv", "_clean.csv")

    df.to_csv(
        f"{processed_folder}/{output_name}",
        index=False
    )

    print(f"Created {output_name}")