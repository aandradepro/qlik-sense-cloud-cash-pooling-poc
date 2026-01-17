import pandas as pd
from pathlib import Path

# ======================================================
# CONFIG
# ======================================================

DATA_PATH = Path("../data/raw/")
EXPECTED_MONTHS = 36
SCENARIOS = {"PRE", "POST"}

errors = []
warnings = []

def fail(msg):
    errors.append(msg)

def warn(msg):
    warnings.append(msg)

# ======================================================
# LOAD DATA
# ======================================================

holding = pd.read_csv(DATA_PATH / "holding.csv")
company = pd.read_csv(DATA_PATH / "company.csv")
country = pd.read_csv(DATA_PATH / "country.csv")
currency = pd.read_csv(DATA_PATH / "currency.csv")
cost_center = pd.read_csv(DATA_PATH / "cost_center.csv")
exchange_rate = pd.read_csv(DATA_PATH / "exchange_rate.csv", parse_dates=["calendar_date"])
cash_position = pd.read_csv(DATA_PATH / "cash_position.csv", parse_dates=["calendar_date"])

# ======================================================
# 1. STRUCTURAL CHECKS
# ======================================================

# PK uniqueness
if holding.holding_id.duplicated().any():
    fail("Duplicate holding_id found")

if company.company_id.duplicated().any():
    fail("Duplicate company_id found")

if country.country_code.duplicated().any():
    fail("Duplicate country_code found")

if currency.currency_code.duplicated().any():
    fail("Duplicate currency_code found")

if cost_center.cost_center_id.duplicated().any():
    fail("Duplicate cost_center_id found")

# ======================================================
# 2. REFERENTIAL INTEGRITY
# ======================================================

if not set(company.holding_id).issubset(set(holding.holding_id)):
    fail("Company with invalid holding_id detected")

if not set(company.country_code).issubset(set(country.country_code)):
    fail("Company with invalid country_code detected")

if not set(cost_center.company_id).issubset(set(company.company_id)):
    fail("Cost center linked to non-existing company")

# ======================================================
# 3. FACT GRAIN
# ======================================================

grain_cols = ["calendar_date", "company_id", "scenario"]
if cash_position.duplicated(subset=grain_cols).any():
    fail("Duplicate rows detected in cash_position grain")

# ======================================================
# 4. SCENARIO COMPLETENESS
# ======================================================

scenario_check = (
    cash_position
    .groupby(["calendar_date", "company_id"])["scenario"]
    .apply(set)
)

if not scenario_check.apply(lambda s: SCENARIOS.issubset(s)).all():
    fail("Missing PRE or POST scenario for some company-month")

# ======================================================
# 5. TIME COVERAGE
# ======================================================

if cash_position.calendar_date.nunique() != EXPECTED_MONTHS:
    fail("Incorrect number of months in cash_position")

# ======================================================
# 6. CURRENCY & FX CHECKS
# ======================================================

if not set(cash_position.local_currency).issubset(set(currency.currency_code)):
    fail("Unknown local_currency found in cash_position")

fx_required = (
    cash_position[["calendar_date", "local_currency"]]
    .drop_duplicates()
    .rename(columns={"local_currency": "from_currency"})
)

fx_merged = fx_required.merge(
    exchange_rate,
    on=["calendar_date", "from_currency"],
    how="left"
)

if fx_merged.fx_rate.isnull().any():
    fail("Missing FX rate for some currency-month")

if (exchange_rate.fx_rate <= 0).any():
    fail("Invalid FX rate (<= 0) detected")

usd_fx = exchange_rate[exchange_rate.from_currency == "USD"]
if not (usd_fx.fx_rate == 1.0).all():
    fail("USD to USD FX rate is not 1.0")

# ======================================================
# 7. VALUE SANITY
# ======================================================

if (cash_position.cash_amount_local <= 0).any():
    fail("Non-positive cash values detected")

# ======================================================
# 8. COST CENTER DISTRIBUTION
# ======================================================

cc_check = (
    cost_center
    .groupby(["company_id", "cost_center_type"])
    .size()
    .unstack(fill_value=0)
)

for ctype in ["OP", "AD", "CO"]:
    if not (cc_check[ctype] == 3).all():
        fail(f"Invalid number of {ctype} cost centers")

# ======================================================
# 9. CONSOLIDATION SANITY (SOFT CHECK)
# ======================================================

group_sum = (
    cash_position
    .groupby(["calendar_date", "scenario"])["cash_amount_local"]
    .sum()
)

if group_sum.nunique() < 2:
    warn("PRE and POST consolidation values are identical — check generation logic")

# ======================================================
# FINAL REPORT
# ======================================================

print("\nDATA QUALITY VALIDATION RESULTS")
print("=" * 40)

if errors:
    print("\n❌ ERRORS:")
    for e in errors:
        print(f"- {e}")
else:
    print("\n✅ No critical errors found")

if warnings:
    print("\n⚠️ WARNINGS:")
    for w in warnings:
        print(f"- {w}")

if errors:
    raise SystemExit("\nValidation failed. Fix errors before loading into Qlik.")

print("\nValidation passed. Data is ready for Qlik Sense.")
