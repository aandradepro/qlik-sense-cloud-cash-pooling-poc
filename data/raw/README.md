# Raw Data – Synthetic Treasury CSV Files

## Purpose of This Folder

This folder contains the **raw synthetic CSV files** used as input for the Qlik Sense Cloud Cash Pooling PoC.

These files simulate **financial extractions from an ERP system**, with structures and semantics inspired by **SAP S/4HANA**, but without using any real or confidential data.

The files in this folder represent the **starting point of the ETL process**.  
No business logic, aggregations, or consolidations should be assumed at this stage.

---

## Design Principles

The raw datasets were designed following these principles:

- **ERP-like structure**  
  Field names and entities resemble common SAP financial concepts to increase realism and recognizability.

- **Minimal transformation**  
  Data is stored close to how it would be extracted from a source system.

- **Monthly granularity**  
  All financial values are monthly, aligned with treasury reporting cycles.

- **Multi-company and multi-country**  
  Data supports consolidation scenarios required for Cash Pooling.

- **Before / After scenario support**  
  Fields allow distinguishing pre- and post-Cash Pooling situations.

---

## Overview of Raw CSV Files

### 1. `treasury_cash_position.csv`

**Description**  
Contains the monthly cash position per company, country, and cost center.

This is the **main fact dataset** used to analyze Cash Pooling effects.

**Grain**
- One record per:
  - Company
  - Country
  - Cost Center
  - Month

**Key Fields**

| Field Name | Description |
|-----------|------------|
| company_code | Legal entity identifier (SAP-like Company Code) |
| company_name | Company description |
| country | Country of operation |
| cost_center | Cost center identifier |
| fiscal_year | Fiscal year |
| fiscal_month | Fiscal month (1–12) |
| currency | Local currency |
| opening_balance | Cash balance at the beginning of the month |
| cash_in | Total cash inflows during the month |
| cash_out | Total cash outflows during the month |
| closing_balance | Cash balance at the end of the month |
| pooling_scenario | Flag indicating `PRE_POOLING` or `POST_POOLING` |

---

### 2. `companies.csv`

**Description**  
Master data for legal entities within the group.

**Purpose**
- Supports consolidation logic
- Defines relationship between subsidiaries and holding

**Key Fields**

| Field Name | Description |
|-----------|------------|
| company_code | Company identifier |
| company_name | Company name |
| parent_company | Holding or parent company code |
| country | Country of registration |
| local_currency | Company local currency |

---

### 3. `cost_centers.csv`

**Description**  
Master data for cost centers used in treasury analysis.

**Key Fields**

| Field Name | Description |
|-----------|------------|
| cost_center | Cost center identifier |
| cost_center_name | Cost center description |
| company_code | Owning company |
| country | Country |

---

### 4. `countries.csv`

**Description**  
Reference table for countries.

**Key Fields**

| Field Name | Description |
|-----------|------------|
| country | Country code or name |
| region | Geographic region |
| reporting_currency | Currency used for reporting |

---

### 5. `currencies.csv`

**Description**  
Reference table for currencies used in the PoC.

**Key Fields**

| Field Name | Description |
|-----------|------------|
| currency | Currency code (e.g., USD, EUR) |
| currency_name | Currency description |
| exchange_rate_to_group | Exchange rate to group reporting currency |

---

## Relationship to the ETL Process

- Files in this folder are **loaded as-is** into Qlik Sense Cloud.
- All transformations, calculations, and consolidation logic are implemented **in the ETL layer**.
- No derived metrics should be calculated directly from raw files.

Detailed transformation logic is documented in: etl/etl_decisions.md

---

## Assumptions and Limitations

- Data is **synthetic and simplified** for demonstration purposes.
- Exchange rates are static and simplified.
- Fiscal calendar assumes standard calendar months.
- The structure is designed for clarity, not full SAP financial complexity.

These assumptions are **intentional and documented** to keep the PoC focused on analytics and governance.

---

## Next Steps

Planned next activities related to raw data:

1. Generate sample CSV files based on the layouts described here  
2. Validate relationships and keys  
3. Load data into Qlik Sense Cloud and start ETL scripting  

---

## Disclaimer

All datasets in this folder are fictional and created solely for portfolio and demonstration purposes.


