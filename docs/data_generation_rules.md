# Data Generation Rules — Cash Pooling PoC (v2)

## 1. Objective

The purpose of this dataset is to simulate a **multinational treasury environment** operating under two scenarios:

- **PRE Cash Pooling** (decentralized cash management)
- **POST Cash Pooling** (centralized cash pooling by holding)

The data must support:
- Executive decision-making
- Clear PRE vs POST comparison
- Consolidation by holding, country, and currency
- FX conversion and volatility analysis
- Governance-oriented analytics design

This is an **analytical Proof of Concept**, not an accounting or transactional system.

---

## 2. Time Scope

| Rule | Definition |
|---|---|
| Period | **36 months** |
| Frequency | Monthly |
| Calendar Type | Fiscal |
| Fiscal Year Start | April |
| Dates | Month-end only |

---

## 3. Organizational Structure

### 3.1 Holdings

| Holding ID | Holding Name |
|---|---|
| H001 | Global Manufacturing Group |
| H002 | Global Services Group |

---

### 3.2 Companies

| Rule | Value |
|---|---|
| Companies per Holding | 3 |
| Total Companies | 6 |
| Company IDs | C001 – C006 |
| Relationship | Each company belongs to exactly one holding |

---

## 4. Countries

| Country | Code | Local Currency |
|---|---|---|
| Brazil | BR | BRL |
| United States | US | USD |
| Germany | DE | EUR |
| United Kingdom | UK | GBP |
| Mexico | MX | MXN |

Rules:
- Each company belongs to one country
- Holdings operate in at least three countries
- Local currency equals country currency

---

## 5. Cost Centers

### 5.1 Cost Center Types

| Type | Code |
|---|---|
| Operational | OP |
| Administrative | AD |
| Commercial | CO |

---

### 5.2 Cost Centers per Company

Each company contains **9 cost centers**:

| Type | Cost Centers |
|---|---|
| Operational | OP01, OP02, OP03 |
| Administrative | AD01, AD02, AD03 |
| Commercial | CO01, CO02, CO03 |

Important:
- Cost centers **do not increase fact table granularity**
- They are used for:
  - Filtering
  - Drill-down
  - Governance and dimensional modeling

---

## 6. Currency and FX Rules

| Rule | Definition |
|---|---|
| Group Currency | USD |
| FX Type | Monthly Average |
| FX Frequency | Monthly |
| Volatility | Low to moderate |
| Currency Pairs | BRL, EUR, GBP, MXN → USD |

USD → USD = 1.0 (fixed)

---

## 7. Core Fact — Cash Position

### 7.1 Grain

| Dimension | Level |
|---|---|
| Company | Monthly |
| Scenario | PRE / POST |
| Currency | Local |
| Cost Center | Associated (not exploded) |

---

### 7.2 Mandatory Fields

- FiscalYear  
- FiscalMonth  
- CalendarDate  
- HoldingID  
- CompanyID  
- CountryCode  
- LocalCurrency  
- CashAmount_Local  
- Scenario (PRE / POST)

---

## 8. Financial Logic

### 8.1 PRE Cash Pooling

- Decentralized cash management
- Excess liquidity per company
- Always positive balances
- Relatively stable monthly patterns

Indicative average balances:
- Brazil: BRL 8M – 12M
- USA: USD 4M – 7M
- Germany: EUR 3M – 6M
- United Kingdom: GBP 3M – 5M
- Mexico: MXN 60M – 90M

---

### 8.2 POST Cash Pooling

Principles:
- Cash centralized by holding
- Operational activity unchanged
- Reduced idle cash

Reduction rules:
- Average reduction: **20%**
- Acceptable range: 15% – 25%
- Variability allowed by company and month

Consolidated balances must be:
- Lower than PRE
- More stable
- Clearly visible at holding level

---

## 9. Consistency Rules (Mandatory)

- POST aggregated cash must never exceed PRE
- No negative cash balances
- FX rates consistent within the same month
- No missing months
- Fiscal calendar integrity must be preserved

---

## 10. Expected Metrics (Emergent)

The data must naturally enable:

- Total Cash (PRE vs POST)
- Cash Reduction (absolute and %)
- Average Monthly Cash
- Cash by Holding / Country
- FX Impact isolation
- Volatility reduction over time

---

## 11. Out of Scope

The dataset does **not** need to:
- Simulate daily cash flows
- Contain bank transactions
- Follow IFRS accounting rules
- Represent bank statements

This PoC focuses on **analytics value**, not accounting compliance.

---

## 12. Expected Outcome

At the end of this process:
- CSV files are self-explanatory
- Dashboards clearly demonstrate value
- A CFO understands the impact in under 3 minutes
- An analytics architect recognizes governance and design quality
