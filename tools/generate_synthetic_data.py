from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

# ======================================================
# 1. GLOBAL PARAMETERS (GOVERNED & DETERMINISTIC)
# ======================================================

SEED = 42
np.random.seed(SEED)

MONTHS = 36
END_DATE = date.today() - relativedelta(months=-1*(MONTHS + 1))
START_DATE = END_DATE.replace(day=1)
COUNTRIES = {
    "BR": {"name": "Brazil", "currency": "BRL", "region": "LATAM"},
    "US": {"name": "United States", "currency": "USD", "region": "NA"},
    "DE": {"name": "Germany", "currency": "EUR", "region": "EU"},
    "UK": {"name": "United Kingdom", "currency": "GBP", "region": "EU"},
    "MX": {"name": "Mexico", "currency": "MXN", "region": "LATAM"},
}

HOLDING_ID = "HOLD01"
HOLDING_NAME = "Global Holdings Inc."
REPORTING_CURRENCY = "USD"

SCENARIOS = ["PRE", "POST"]

COMPANIES_PER_COUNTRY = 2
COST_CENTER_TYPES = {
    "OP": 3,
    "AD": 3,
    "CO": 3,
}

# ======================================================
# 2. TIME DIMENSION
# ======================================================

dates = [START_DATE + relativedelta(months=i) for i in range(MONTHS)]

calendar_df = pd.DataFrame({
    "calendar_date": dates,
    "fiscal_year": [d.year for d in dates],
    "fiscal_month": [d.month for d in dates],
})

# ======================================================
# 3. HOLDING
# ======================================================

holding_df = pd.DataFrame([{
    "holding_id": HOLDING_ID,
    "holding_name": HOLDING_NAME,
    "reporting_currency": REPORTING_CURRENCY
}])

# ======================================================
# 4. COUNTRY
# ======================================================

country_df = pd.DataFrame([
    {
        "country_code": k,
        "country_name": v["name"],
        "country_currency": v["currency"],
        "region": v["region"],
    }
    for k, v in COUNTRIES.items()
])

# ======================================================
# 5. COMPANY
# ======================================================

companies = []
company_counter = 1

for country_code, cdata in COUNTRIES.items():
    for i in range(COMPANIES_PER_COUNTRY):
        companies.append({
            "company_id": f"C{company_counter:03d}",
            "company_name": f"{cdata['name']} Co {i+1}",
            "holding_id": HOLDING_ID,
            "country_code": country_code,
            "company_currency": cdata["currency"],
            "company_type": "Manufacturing" if i % 2 == 0 else "Services",
        })
        company_counter += 1

company_df = pd.DataFrame(companies)

# ======================================================
# 6. COST CENTER
# ======================================================

cost_centers = []

for _, row in company_df.iterrows():
    for cc_type, qty in COST_CENTER_TYPES.items():
        for i in range(1, qty + 1):
            cost_centers.append({
                "cost_center_id": f"{row.company_id}_{cc_type}{i}",
                "cost_center_type": cc_type,
                "cost_center_name": f"{cc_type} Cost Center {i}",
                "cost_center_company_id": row.company_id,
            })

cost_center_df = pd.DataFrame(cost_centers)

# ======================================================
# 6.1 COST CENTER LOOKUPS (DERIVED STRUCTURES)
# ======================================================

# Map cost centers per company (used in fact generation)
cost_centers_by_company = (
    cost_center_df
    .groupby("cost_center_company_id")["cost_center_id"]
    .apply(list)
    .to_dict()
)

# ======================================================
# 7. CURRENCY
# ======================================================

currency_df = pd.DataFrame([
    {"currency_code": v["currency"], "currency_name": v["currency"]}
    for v in COUNTRIES.values()
]).drop_duplicates()

# ======================================================
# 8. EXCHANGE RATE (MONTHLY AVG TO USD)
# ======================================================

fx_rows = []

for _, row in calendar_df.iterrows():
    for cur in currency_df.currency_code:
        fx_rows.append({
            "calendar_date": row.calendar_date,
            "fiscal_year": row.fiscal_year,
            "fiscal_month": row.fiscal_month,
            "from_currency": cur,
            "to_currency": "USD",
            "fx_rate": 1.0 if cur == "USD" else round(np.random.uniform(0.5, 1.5), 4),
        })

exchange_rate_df = pd.DataFrame(fx_rows)

# ======================================================
# 9. CASH POSITION (FACT)
# ======================================================

fact_rows = []

for _, comp in company_df.iterrows():
    base_cash = np.random.uniform(5_000, 25_000)
    
    company_cost_centers = cost_centers_by_company[comp.company_id]
    num_cc = len(company_cost_centers)

    for _, cal in calendar_df.iterrows():
        for scenario in SCENARIOS:
            adjustment = 1.0 if scenario == "PRE" else np.random.uniform(1.05, 1.25)
            total_cash = base_cash * adjustment
#TODO: Divide cash equally among cost centers, could be improved to a more realistic distribution.
            cash_per_cc = total_cash / num_cc

            for cost_center_id in company_cost_centers:
                fact_rows.append({
                    "date": cal.calendar_date,
                    "fiscal_year": cal.fiscal_year,
                    "fiscal_month": cal.fiscal_month,
                    "scenario": scenario,
                    "holding_id": HOLDING_ID,
                    "company_id": comp.company_id,
                    "cost_center_id": cost_center_id,
                    "country_code": comp.country_code,
                    "cash_currency": comp.company_currency,
                    "cash_amount": round(cash_per_cc, 2),
                })

cash_position_df = pd.DataFrame(fact_rows)

# ======================================================
# 10. EXPORT CSVs
# ======================================================

# Path absoluto baseado na localização do arquivo
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_PATH = BASE_DIR / "data" / "raw"
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

holding_df.to_csv(OUTPUT_PATH / "holding.csv", index=False)
company_df.to_csv(OUTPUT_PATH / "company.csv", index=False)
country_df.to_csv(OUTPUT_PATH / "country.csv", index=False)
cost_center_df.to_csv(OUTPUT_PATH / "cost_center.csv", index=False)
currency_df.to_csv(OUTPUT_PATH / "currency.csv", index=False)
exchange_rate_df.to_csv(OUTPUT_PATH / "exchange_rate.csv", index=False)
cash_position_df.to_csv(OUTPUT_PATH / "cash_position.csv", index=False)

print("Synthetic Cash Pooling datasets generated successfully.")
