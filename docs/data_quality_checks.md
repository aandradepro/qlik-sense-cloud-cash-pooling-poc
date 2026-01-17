# Data Quality Checks — Qlik Sense Governance

This document defines the **expected data quality checks**
implemented or validated within **Qlik Sense Cloud**
for the Cash Pooling Analytics Proof of Concept.

The goal is not data cleansing at source,
but **data trust, transparency, and executive confidence**.

---

## 1. Data Quality Philosophy

### Principle
Data quality is treated as:
- A **governance concern**
- A **decision enabler**
- A **shared responsibility**

Checks are designed to:
- Surface issues early
- Prevent silent data corruption
- Make assumptions explicit

---

## 2. Structural Integrity Checks

### 2.1 Primary Key Uniqueness

**Tables Covered**
- holding
- company
- country
- currency
- cost_center

**Check**
- Each primary key must be unique

**Expected Result**
- Zero duplicates

---

### 2.2 Referential Integrity

**Checks**
- Every `company.holding_id` exists in `holding`
- Every `company.country_code` exists in `country`
- Every `cost_center.company_id` exists in `company`

**Expected Result**
- No orphan records

---

## 3. Fact Table Consistency

### 3.1 Grain Validation

**Fact Table**
- cash_position

**Expected Grain**
- Company + Month + Scenario

**Expected Result**
- No duplicate fact rows

---

### 3.2 Scenario Completeness

**Check**
- Every company-month must have:
  - One PRE row
  - One POST row

**Expected Result**
- Balanced scenario coverage

---

## 4. Time Coverage Checks

### 4.1 Continuous Time Series

**Check**
- 36 consecutive months present

**Expected Result**
- No gaps in calendar_date

---

### 4.2 Fiscal Calendar Alignment

**Checks**
- Every fact row maps to a fiscal year
- Every fact row maps to a fiscal month

**Expected Result**
- 100% calendar coverage

---

## 5. Currency and FX Checks

### 5.1 Currency Completeness

**Checks**
- Every cash_position.local_currency exists in currency

**Expected Result**
- No unknown currencies

---

### 5.2 FX Rate Coverage

**Checks**
- Every non-USD currency has:
  - One FX rate per month

**Expected Result**
- No missing FX rates

---

### 5.3 FX Sanity Checks

**Checks**
- fx_rate > 0
- USD → USD rate = 1.0

**Expected Result**
- No invalid conversion factors

---

## 6. Value Sanity Checks

### 6.1 Cash Value Constraints

**Checks**
- cash_amount_local > 0

**Expected Result**
- No zero or negative balances

---

### 6.2 Outlier Detection (Soft Check)

**Check**
- Identify extreme month-over-month variations

**Expected Result**
- Outliers flagged for review, not automatically removed

---

## 7. Consolidation Validation

### 7.1 Company-to-Holding Roll-Up

**Check**
- Holding total = sum of company values

**Expected Result**
- No discrepancies

---

### 7.2 Scenario Delta Consistency

**Check**
- POST ≠ PRE for most months

**Expected Result**
- Visible impact of cash pooling

---

## 8. Dimensional Coverage Checks

### 8.1 Cost Center Distribution

**Check**
- Every company has:
  - 3 OP
  - 3 AD
  - 3 CO cost centers

**Expected Result**
- Consistent dimensional structure

---

## 9. Reload Stability Checks

### 9.1 Record Count Stability

**Check**
- Row counts remain stable across reloads

**Expected Result**
- Variations only when rules change

---

### 9.2 Null Value Monitoring

**Check**
- Monitor unexpected nulls in key fields

**Expected Result**
- Nulls only where explicitly allowed

---

## 10. How Checks Are Surfaced

### Implementation Options
- Hidden governance sheet
- KPI objects with thresholds
- Conditional formatting
- Reload logs

---

## Final Note

Data quality is not about perfection.

It is about:
- Knowing your data
- Trusting your numbers
- Defending your decisions
