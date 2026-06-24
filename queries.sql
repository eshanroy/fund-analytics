-- 1. Top 5 funds by AUM

SELECT scheme_name, aum_crore
FROM "07_scheme_performance"
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per AMFI code

SELECT amfi_code,
       AVG(nav) AS avg_nav
FROM "02_nav_history"
GROUP BY amfi_code;

-- 3. Transaction count by state

SELECT state,
       COUNT(*) AS total_transactions
FROM "08_investor_transactions"
GROUP BY state
ORDER BY total_transactions DESC;

-- 4. Funds with expense ratio below 1%

SELECT scheme_name,
       expense_ratio_pct
FROM "07_scheme_performance"
WHERE expense_ratio_pct < 1;

-- 5. Total investment by transaction type

SELECT transaction_type,
       SUM(amount_inr) AS total_amount
FROM "08_investor_transactions"
GROUP BY transaction_type;

-- 6. Average 1-Year Return by Category

SELECT category,
       AVG(return_1yr_pct) AS avg_return
FROM "07_scheme_performance"
GROUP BY category;

-- 7. Top 10 Investors by Investment Amount

SELECT investor_id,
       SUM(amount_inr) AS total_investment
FROM "08_investor_transactions"
GROUP BY investor_id
ORDER BY total_investment DESC
LIMIT 10;

-- 8. Transactions by KYC Status

SELECT kyc_status,
       COUNT(*) AS total
FROM "08_investor_transactions"
GROUP BY kyc_status;

-- 9. Average AUM by Fund House

SELECT fund_house,
       AVG(aum_crore) AS avg_aum
FROM "07_scheme_performance"
GROUP BY fund_house
ORDER BY avg_aum DESC;

-- 10. Highest Returning Funds (3 Year)

SELECT scheme_name,
       return_3yr_pct
FROM "07_scheme_performance"
ORDER BY return_3yr_pct DESC
LIMIT 10;