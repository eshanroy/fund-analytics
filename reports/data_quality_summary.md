DATA QUALITY SUMMARY

Dataset Overview
---------------
01_fund_master.csv           -> (40, 15)
02_nav_history.csv          -> (46000, 3)
03_aum_by_fund_house.csv    -> (90, 5)
04_monthly_sip_inflows.csv  -> (48, 6)
05_category_inflows.csv     -> (144, 3)
06_industry_folio_count.csv -> (21, 6)
07_scheme_performance.csv   -> (40, 19)
08_investor_transactions.csv -> (32778, 13)
09_portfolio_holdings.csv   -> (322, 8)
10_benchmark_indices.csv    -> (8050, 3)

Fund Master Analysis
--------------------
Total Fund Houses: 10
Total Schemes: 40

Categories:
- Equity
- Debt

Sub Categories:
- Large Cap
- Small Cap
- Mid Cap
- Flexi Cap
- Large & Mid Cap
- Value
- ELSS
- Index
- Index/ETF
- Liquid
- Gilt
- Short Duration

Risk Categories:
- Low
- Moderate
- High
- Moderately High
- Very High

Data Quality Findings
---------------------
- No missing values found in fund_master dataset.
- No duplicate rows found in fund_master dataset.
- All 40 AMFI codes from fund_master exist in nav_history.
- Dataset relationships appear consistent.
- Fund master can be used as the primary lookup table for further analysis.

Recommendations
---------------
- Validate date formats across all datasets.
- Check for missing values in remaining datasets.
- Verify transaction amounts and NAV values for outliers.
- Create data dictionary for all datasets.