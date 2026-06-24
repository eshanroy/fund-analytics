# Data Dictionary

## 01_fund_master

| Column        | Data Type | Description              |
| ------------- | --------- | ------------------------ |
| amfi_code     | Integer   | Unique AMFI scheme code  |
| fund_house    | Text      | Mutual fund company      |
| scheme_name   | Text      | Scheme name              |
| category      | Text      | Equity or Debt           |
| sub_category  | Text      | Detailed category        |
| plan          | Text      | Regular or Direct        |
| risk_category | Text      | Fund risk classification |

## 02_nav_history

| Column    | Data Type | Description       |
| --------- | --------- | ----------------- |
| amfi_code | Integer   | Scheme identifier |
| date      | Date      | NAV date          |
| nav       | Float     | Net Asset Value   |

## 07_scheme_performance

| Column            | Data Type | Description              |
| ----------------- | --------- | ------------------------ |
| return_1yr_pct    | Float     | 1-year return percentage |
| return_3yr_pct    | Float     | 3-year return percentage |
| return_5yr_pct    | Float     | 5-year return percentage |
| expense_ratio_pct | Float     | Expense ratio percentage |
| aum_crore         | Float     | Assets under management  |

## 08_investor_transactions

| Column           | Data Type | Description              |
| ---------------- | --------- | ------------------------ |
| investor_id      | Text      | Investor identifier      |
| transaction_date | Date      | Transaction date         |
| transaction_type | Text      | SIP, Lumpsum, Redemption |
| amount_inr       | Float     | Transaction amount       |
| state            | Text      | Investor state           |
| kyc_status       | Text      | KYC verification status  |

Source: Bluestock Mutual Fund Analytics Internship Datasets
