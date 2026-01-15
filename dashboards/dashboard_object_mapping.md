# Dashboard Object Mapping  
## Cash Pooling Executive Dashboard – Qlik Sense Cloud

---

## Purpose of This Document

This document maps each logical element of the executive wireframe to **concrete Qlik Sense objects**, including recommended configurations.

The objective is to ensure:
- Consistency between design and implementation
- Governance and repeatability
- Clear translation from business intent to technical build

---

## Global Configuration (Applies to All Objects)

### App Settings
- Default language: English
- Number formatting: Group currency standard
- Date formatting: Fiscal calendar (YYYY-MM)

### Global Filters (Qlik Sense Objects)

| Business Concept | Qlik Object | Field |
|-----------------|------------|-------|
| Fiscal Year | Filter Pane | FiscalYear |
| Country | Filter Pane | Country |
| Holding Company | Filter Pane | Holding |

---

## ZONE 1 – Executive KPIs

### Object Type
**KPI Object** (Standard Qlik Sense KPI)

---

### KPI 1 – Average Cash Balance (Group Currency)

**Qlik Object:** KPI  

**Measure:**
```qlik
Avg(TOTAL <FiscalYearMonth> CashBalance_GroupCurrency)
```

**Subtitle:**  
Average monthly cash balance

---

### KPI 2 – Cash Reduction (Absolute)

**Qlik Object:** KPI  

**Measure:**
```qlik
Avg(
    {<PoolingScenario={'PRE'}>} CashBalance_GroupCurrency
)
-
Avg(
    {<PoolingScenario={'POST'}>} CashBalance_GroupCurrency
)
```

**Subtitle:**  
Before vs After Cash Pooling

---

### KPI 3 – Cash Reduction (%)

**Qlik Object:** KPI  

**Measure:**
```qlik
(
    Avg({<PoolingScenario={'PRE'}>} CashBalance_GroupCurrency)
    -
    Avg({<PoolingScenario={'POST'}>} CashBalance_GroupCurrency)
)
/
Avg({<PoolingScenario={'PRE'}>} CashBalance_GroupCurrency)
```

**Formatting:**  
Percentage, 1 decimal

---

### KPI 4 – Net Cash Movement

**Qlik Object:** KPI  

**Measure:**
```qlik
Sum(NetCashMovement_GroupCurrency)
```

**Subtitle:**  
Consolidated net movement

---

## ZONE 2 – Before vs After Comparison

### Object – Cash Balance Comparison

**Qlik Object:**  
Bar Chart (Grouped)

**Dimensions:**
- PoolingScenario

**Measures:**
- Avg(CashBalance_GroupCurrency)

**Sorting:**
- Custom order: PRE → POST

**Reference Line (Optional):**
- Average PRE balance

---

## ZONE 3 – Time Evolution

### Object – Cash Balance Over Time

**Qlik Object:**  
Line Chart

**Dimensions:**
- FiscalYearMonth

**Measures:**
- Avg(CashBalance_GroupCurrency)

**Settings:**
- Continuous time axis
- No markers (clean executive view)

---

## ZONE 4 – Consolidation & Drill-down

### Object – Consolidated Cash View

**Qlik Object:**  
Bar Chart or Straight Table

**Dimensions (Drill-down Group):**
1. Holding
2. Company

**Measures:**
1. Avg(CashBalance_GroupCurrency)
2. Cash Reduction (Absolute)
3. Cash Reduction (%)

**Cash Reduction Measures:**  
Reuse KPI expressions for consistency.

---

## Interaction Rules

### Enabled
- Drill-down (Holding → Company)
- Cross-selection between charts

### Disabled / Not Exposed
- PoolingScenario as filter pane
- Currency as filter pane

---

## Performance & Governance Notes

- All measures rely on **pre-calculated fact fields**
- No complex chart-level calculations
- Set Analysis used only for scenario comparison

---

## Validation Checklist

| Item | Status |
|----|----|
| KPIs reflect group currency | ✔ |
| Scenario comparison protected | ✔ |
| Drill-down works as expected | ✔ |
| Filters do not break narrative | ✔ |

---

## Final Note

This object mapping ensures that the executive dashboard:
- Is fully aligned with the logical wireframe
- Can be built consistently across environments
- Reflects senior-level analytics design principles
