# Data Model – FX Cash Position PoC

## 1. Overview

This document describes the logical data model used in the **FX Cash Position Proof of Concept (PoC)** built in Qlik.

The model is designed to:
- Analyze cash positions across companies, cost centers, countries, and holdings
- Support multi-currency reporting
- Enable **FX exposure and sensitivity analysis**
- Ensure **scenario isolation** (no aggregation across scenarios)
- Apply exchange rates **during the load process**, not at reporting time

The model follows a **star-schema-oriented analytical design**, with one central fact table and multiple conformed dimensions.

---

## 2. Fact Table

### FCT_CashPosition

The central fact table stores cash balances and reporting amounts already converted using the applicable exchange rate.

**Grain**
- One record per:
  - Date
  - Company
  - Cost Center
  - Scenario
  - Cash Currency

**Fields**
- `date`  
  Reference date of the cash position

- `company_id`  
  Company identifier

- `cost_center_id`  
  Cost center identifier

- `scenario`  
  Business scenario (e.g. Actual, Forecast, Budget)  
  ⚠️ **Critical field – scenarios must never be aggregated**

- `cash_currency`  
  Original currency of the cash amount

- `cash_amount`  
  Amount in local (transaction) currency

- `fx_rate_applied`  
  Exchange rate applied during the load process

- `reporting_amount`  
  Amount converted to the reporting currency

**Design Notes**
- FX conversion is **materialized** in the fact table
- No exchange rate calculations are performed at visualization time
- Enables reconciliation and auditability of FX logic

---

## 3. Dimension Tables

### DIM_Calendar

Provides time-related attributes for analysis and aggregation.

**Fields**
- `date` (PK)
- `fiscal_year`
- `fiscal_month`

---

### DIM_Company

Stores company master data and its relationship to holdings and countries.

**Fields**
- `company_id` (PK)
- `country_code`
- `holding_id`
- `company_name`
- `company_currency`
- `company_type`

---

### DIM_CostCenter

Describes cost center structures and classifications.

**Fields**
- `cost_center_id` (PK)
- `cost_center_name`
- `cost_center_type`
- `cost_center_company_id`

---

### DIM_Country

Geographical reference dimension.

**Fields**
- `country_code` (PK)
- `country_name`
- `region`

---

### DIM_Holding

Represents holding-level entities and defines the **reporting currency**.

**Fields**
- `holding_id` (PK)
- `holding_name`
- `reporting_currency`

**Design Note**
- Reporting currency is defined at holding level
- All reporting amounts are aligned to this currency

---

## 4. Exchange Rate Table (Technical)

### ExchangeRate

Technical table used **only during the load process** to apply FX conversion.

**Fields**
- `rate_date`
- `from_currency`
- `to_currency`
- `exchange_rate`

**Design Principles**
- Not exposed as an analytical dimension
- Not associated directly with the data model
- Used to:
  - Calculate `fx_rate_applied`
  - Populate `reporting_amount`

This approach avoids:
- Circular references
- Incorrect aggregations
- Runtime FX inconsistencies

---

## 5. Key Modeling Principles

### Scenario Governance
- `scenario` is part of the fact table grain
- Visualizations **must always include scenario as a dimension or filter**
- Aggregating across scenarios is considered invalid

---

### FX Governance
- FX conversion is deterministic and reproducible
- Each record explicitly stores the rate applied
- Enables validation, audit, and reconciliation

---

### Exposure Analysis Readiness
The model supports FX exposure analysis by:
- Comparing `cash_currency` vs `reporting_currency`
- Classifying balances as:
  - FX Exposed
  - Not FX Exposed

This logic is implemented at the visualization layer without reapplying FX.

---

## 6. Intended Usage

This model is designed for:
- FX exposure and sensitivity analysis
- Cash position reporting
- Governance and validation dashboards
- Proof-of-concept demonstrations with enterprise-grade modeling practices

---

## 7. Status

- Model type: **Proof of Concept (PoC)**
- Architecture: **Analytical / Star Schema**
- Tool: **Qlik**
- FX Strategy: **Pre-calculated, load-time conversion**

---