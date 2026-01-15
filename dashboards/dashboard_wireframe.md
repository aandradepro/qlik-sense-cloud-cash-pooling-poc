# Executive Dashboard – Logical Wireframe  
## Cash Pooling PoC | Qlik Sense Cloud

---

## 1. Dashboard Objective (Single Sentence)

Enable executives to quickly assess whether Cash Pooling reduced idle cash and improved treasury efficiency, at group and entity level.

---

## 2. Global Context (Applies to Entire Dashboard)

### Global Selections (Top Bar)

- Fiscal Year
- Country
- Holding Company

> Purpose: define organizational and temporal context without breaking the analytical narrative.

---

## 3. Layout Structure (Top → Bottom)

The dashboard is organized in **four horizontal logical zones**.

---

## ZONE 1 – Executive KPIs (Immediate Insight)

**Purpose:**  
Provide instant, high-level answers without interaction.

### Objects in This Zone

| Position | Object Type | KPI |
|--------|-------------|-----|
| 1 | KPI | Average Cash Balance (Group Currency) |
| 2 | KPI | Cash Reduction – Absolute |
| 3 | KPI | Cash Reduction – % |
| 4 | KPI | Net Cash Movement |

### Logical Notes
- All KPIs calculated in **group currency**
- Values reflect **Before vs After Cash Pooling**
- No dimensions exposed

---

## ZONE 2 – Core Business Question (Impact Visualization)

**Purpose:**  
Visually prove the impact of Cash Pooling.

### Object 1 – Before vs After Comparison

**Type:**  
Grouped Bar Chart (or Side-by-Side Bars)

**Dimensions:**
- Pooling Scenario (PRE / POST)

**Measures:**
- Average Monthly Cash Balance (Group Currency)

**Key Question Answered:**  
> Did Cash Pooling reduce the average cash balance?

---

## ZONE 3 – Time Validation (Confidence & Trend)

**Purpose:**  
Build trust in the numbers and reveal patterns.

### Object 2 – Cash Balance Over Time

**Type:**  
Line Chart

**Dimensions:**
- Fiscal Year-Month

**Measures:**
- Average Monthly Cash Balance (Group Currency)

**Key Question Answered:**  
> Is the observed impact consistent over time or driven by anomalies?

---

## ZONE 4 – Consolidation & Accountability

**Purpose:**  
Enable governance and accountability without losing the executive view.

### Object 3 – Consolidation View

**Type:**  
Bar Chart or Table (depending on screen space)

**Dimensions:**
1. Holding Company
2. Company (Drill-down)

**Measures:**
- Average Monthly Cash Balance
- Cash Reduction (Absolute)
- Cash Reduction (%)

**Key Questions Answered:**
- Which holdings benefit the most from Cash Pooling?
- Are there entities that still concentrate excess cash?

---

## 4. Interaction Model

### Allowed Interactions
- Drill-down: Holding → Company
- Cross-filtering via chart selection

### Explicitly Disabled
- Scenario selection (PRE / POST)
- Currency selection

> Rationale: protect the analytical story and avoid misinterpretation.

---

## 5. Information Density Rules

- Maximum 4 KPIs
- Maximum 3 analytical charts
- No more than 2 measures per chart (except tables)

---

## 6. Visual Hierarchy Rules

1. KPIs must be readable in < 5 seconds
2. Impact comparison must be immediately visible
3. Trends support, not compete with, KPIs
4. Detail appears only after user intent (drill-down)

---

## 7. What This Dashboard Is NOT

- Not an operational cash management tool
- Not a forecasting engine
- Not a bank-account-level analysis

This dashboard is an **executive impact assessment tool**.

---

## 8. Portfolio Positioning Statement

This wireframe demonstrates:
- Executive-first thinking
- Governance-oriented analytics
- Clear separation between data, logic and visualization
- Alignment with modern cloud analytics practices
