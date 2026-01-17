# Raw Data — CSV Structure

This directory contains the **raw input datasets** used in the Cash Pooling Proof of Concept.

All data is **synthetically generated**, following explicit business rules defined in  
`docs/data_generation_rules.md`.

The CSV files are designed to:
- Resemble a **SAP S/4HANA–like data model**
- Support **governed analytics** in Qlik Sense Cloud
- Enable **PRE vs POST Cash Pooling** analysis
- Serve as a reproducible and transparent data foundation

---

## Directory Purpose

The `/data/raw` layer represents the **ingestion layer** of the analytics pipeline:

- No transformations
- No aggregations
- No currency conversion
- No business logic applied

All business rules and calculations are applied **inside Qlik Sense**.

---

## CSV Files Overview

| File | Type | Description |
|---|---|---|
| `holding.csv` | Dimension | Holding structure for consolidation |
| `company.csv` | Dimension | Company (Company Code) master data |
| `country.csv` | Dimension | Country and local currency |
| `cost_center.csv` | Dimension | Cost centers per company |
| `currency.csv` | Dimension | Currency master data |
| `exchange_rate.csv` | Fact (auxiliary) | Monthly FX rates to USD |
| `cash_position.csv` | **Fact (core)** | Monthly cash position (PRE / POST) |

---

## 1. `holding.csv`

**Grain:** One row per holding.

| Field | Type | Description |
|---|---|---|
| holding_id | STRING | Holding identifier (PK) |
| holding_name | STRING | Holding name |
| reporting_currency | STRING | Group reporting currency (USD) |

---

## 2. `company.csv`

**Grain:** One row per company.

| Field | Type | Description |
|---|---|---|
| company_id | STRING | Company identifier (PK) |
| company_name | STRING | Company name |
| holding_id | STRING | Holding identifier (FK) |
| country_code | STRING | Country code (FK) |
| local_currency | STRING | Local company currency |
| company_type | STRING | Manufacturing / Services (optional) |

> Note: Some redundancy (e.g., local_currency) is intentional and reflects
> SAP-like master data design.

---

## 3. `country.csv`

**Grain:** One row per country.

| Field | Type | Description |
|---|---|---|
| country_code | STRING | Country code (PK) |
| country_name | STRING | Country name |
| currency_code | STRING | Local currency |
| region | STRING | Geographic region |

---

## 4. `cost_center.csv`

**Grain:** One row per cost center **per company**.

Each company has **9 cost centers**:
- 3 Operational
- 3 Administrative
- 3 Commercial

| Field | Type | Description |
|---|---|---|
| cost_center_id | STRING | Cost center code |
| cost_center_type | STRING | OP / AD / CO |
| cost_center_name | STRING | Cost center description |
| company_id | STRING | Company identifier (FK) |

> Cost centers are **not part of the fact table grain**.  
> They are used for filtering, drill-down, and governance.

---

## 5. `currency.csv`

**Grain:** One row per currency.

| Field | Type | Description |
|---|---|---|
| currency_code | STRING | Currency code (PK) |
| currency_name | STRING | Currency name |

---

## 6. `exchange_rate.csv`

**Grain:** One row per currency **per month**.

Contains **monthly average FX rates** to USD.

| Field | Type | Description |
|---|---|---|
| calendar_date | DATE | Month-end date |
| fiscal_year | INTEGER | Fiscal year |
| fiscal_month | INTEGER | Fiscal month |
| from_currency | STRING | Source currency |
| to_currency | STRING | Target currency (USD) |
| fx_rate | DECIMAL | FX rate |

Rules:
- Same FX rate applies to all companies in the same month
- USD → USD rate is always 1.0

---

## 7. `cash_position.csv` (Core Fact)

**Grain:**  
**Company + Month + Scenario**

This is the **main fact table** of the PoC.

| Field | Type | Description |
|---|---|---|
| calendar_date | DATE | Month-end date |
| fiscal_year | INTEGER | Fiscal year |
| fiscal_month | INTEGER | Fiscal month |
| scenario | STRING | PRE or POST |
| holding_id | STRING | Holding identifier |
| company_id | STRING | Company identifier |
| country_code | STRING | Country code |
| local_currency | STRING | Local currency |
| cash_amount_local | DECIMAL | Cash balance (local currency) |

Important:
- Values are always **positive**
- No currency conversion is applied here
- PRE and POST scenarios coexist in the same table

---

## Data Modeling Notes

- The model intentionally uses **controlled redundancy**
- No transactional data is included
- All calculations (FX conversion, consolidation, KPIs) are performed in Qlik
- The structure favors **clarity, performance, and executive analytics**

---

## Usage Disclaimer

These datasets are:
- Fully synthetic
- Designed exclusively for analytics demonstrations
- Not intended for accounting or regulatory reporting

---

## Next Steps

After loading this data into Qlik Sense Cloud:
1. Apply governed transformations
2. Implement FX conversion
3. Apply holding-level consolidation
4. Build executive dashboards
