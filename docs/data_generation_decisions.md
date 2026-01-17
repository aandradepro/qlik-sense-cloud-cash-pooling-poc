# Data Generation Decisions — Design Rationale

This document explains the **design decisions** behind the synthetic data generation
used in the **Cash Pooling Analytics Proof of Concept**.

The goal is not to simulate accounting accuracy, but to create a **realistic, controllable,
and analytically meaningful dataset** that enables executive decision-making in
Qlik Sense Cloud.

---

## 1. Guiding Principles

The data generation follows five core principles:

1. **Executive relevance over transactional detail**
2. **Controlled complexity**
3. **Transparency and reproducibility**
4. **Governance-first analytics**
5. **Cloud-native modeling**

These principles guided every decision described below.

---

## 2. Why Synthetic Data

### Decision
All datasets are **100% synthetic**, with no real company data.

### Rationale
- Eliminates confidentiality and compliance risks
- Enables public sharing (GitHub + LinkedIn)
- Allows deterministic behavior (same inputs → same outputs)
- Focuses the PoC on **analytics architecture**, not data sourcing

This aligns with modern analytics portfolios, where **how data is modeled and governed**
is more important than where it comes from.

---

## 3. Time Horizon: 36 Months

### Decision
The dataset spans **36 consecutive months**.

### Rationale
- Enables trend, seasonality, and rolling KPIs
- Supports fiscal calendars
- Allows clear comparison of PRE vs POST Cash Pooling
- Matches common treasury planning horizons

Shorter periods would limit executive insight; longer periods would add complexity
without analytical benefit.

---

## 4. Organizational Scope

### 4.1 Multinational Structure

**Decision**
- 1 Holding
- Multiple Companies
- 5 Countries

**Rationale**
Cash pooling value only becomes visible in **multi-entity, multi-country** scenarios.
This structure allows:
- FX exposure
- Cash fragmentation
- Consolidation effects

---

### 4.2 Company-Level Grain

**Decision**
The **company** is the lowest organizational grain in the fact table.

**Rationale**
- Matches treasury decision-making
- Avoids unnecessary transaction-level noise
- Enables clear consolidation logic
- Reflects common SAP Treasury reporting structures

Cost centers are included as dimensions but **not part of the fact grain**.

---

## 5. Cash Pooling Scenarios (PRE / POST)

### Decision
Both **PRE** and **POST** scenarios coexist in the same fact table,
distinguished by a `scenario` field.

### Rationale
- Enables side-by-side comparison
- Avoids duplicated data models
- Simplifies KPI definitions
- Supports scenario-based filtering

This reflects how modern analytics platforms handle scenario analysis.

---

## 6. Cash Value Design

### Decision
- Cash values are always **positive**
- Generated in **local currency**
- No overdrafts or negative balances

### Rationale
The PoC focuses on:
- Liquidity optimization
- Cash concentration efficiency
- FX and consolidation impact

Negative balances would introduce financing logic
outside the scope of the demonstration.

---

## 7. Currency and FX Design

### Decision
- FX rates are monthly averages
- Same rate applies to all companies per month
- All conversions target USD

### Rationale
- Simplifies FX logic while remaining realistic
- Matches executive-level reporting needs
- Avoids daily volatility noise
- Reflects typical treasury dashboards

USD was chosen as a neutral reporting currency.

---

## 8. Cost Center Design

### Decision
Each company has:
- 3 Operational cost centers
- 3 Administrative cost centers
- 3 Commercial cost centers

### Rationale
Cost centers exist to:
- Demonstrate dimensional governance
- Enable filtering and drill-down
- Reflect real SAP master data structures

They are **not used for financial allocation** in this PoC,
by design.

---

## 9. SAP-Inspired Modeling Choices

### Decision
The data model intentionally includes:
- Redundant attributes (e.g., currency in multiple tables)
- Explicit master data tables
- Clear foreign key relationships

### Rationale
This mirrors **SAP S/4HANA analytical models**, where:
- Redundancy improves usability
- Master data is explicit
- Business context is preserved

The goal is familiarity for SAP professionals,
not strict normalization.

---

## 10. What Was Explicitly Excluded

The following were **intentionally not included**:

- Transaction-level cash movements
- Intercompany loan mechanics
- Interest calculations
- Bank-level granularity
- Daily balances

### Rationale
Including these would:
- Obscure the core message
- Reduce executive readability
- Shift focus away from analytics design

This PoC demonstrates **decision intelligence**, not accounting engines.

---

## 11. Alignment with Executive Analytics

The generated data enables:
- Liquidity visibility
- Cash concentration impact
- FX exposure analysis
- Before/after process comparison
- Holding-level decision support

This aligns with the stated positioning:
> **“Specialist in modern analytics and cloud governance.”**

---

## 12. Reproducibility

All generation rules are:
- Documented
- Deterministic
- Version-controlled

Anyone can regenerate the same datasets
using the documented rules.

This is a **key governance principle** of the project.

---

## Final Note

These decisions are not about realism at any cost.

They are about:
- **Clarity**
- **Control**
- **Analytical value**
- **Executive storytelling**

Exactly what a modern analytics PoC should deliver.
