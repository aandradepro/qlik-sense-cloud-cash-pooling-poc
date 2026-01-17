# ETL Load Decisions — Qlik Sense Script Design

This document describes the **design decisions and rationale** behind the
Qlik Sense load script used in the **Cash Pooling Analytics Proof of Concept**.

The focus is on **governed, scalable, and cloud-ready scripting practices**,
not on tool-specific syntax details.

---

## 1. ETL Philosophy

### Decision
All business logic is implemented **inside Qlik Sense**, with no preprocessing
outside the platform.

### Rationale
- Demonstrates Qlik as an **end-to-end analytics platform**
- Keeps raw data immutable
- Improves traceability and governance
- Aligns with cloud-native analytics practices

The `/data/raw` layer remains untouched.

---

## 2. Layered Script Structure

### Decision
The load script is organized into logical layers:

1. **Raw Load**
2. **Standardization**
3. **Conformed Dimensions**
4. **Governed Facts**
5. **Calendar & Auxiliary Tables**

### Rationale
- Improves readability and maintenance
- Enables selective reloads
- Mirrors enterprise ETL frameworks
- Facilitates onboarding of other developers

---

## 3. Explicit Control of Grain

### Decision
The grain of the fact table is **explicitly enforced** in the script.

**Fact Grain:**  
Company + Month + Scenario

### Rationale
- Prevents accidental aggregation
- Ensures KPI consistency
- Avoids data duplication during joins
- Makes assumptions transparent

---

## 4. No Implicit Joins

### Decision
All joins are:
- Explicit
- Intentional
- Documented

Synthetic keys and auto-concatenation are avoided.

### Rationale
- Prevents hidden data model behavior
- Improves debugging
- Aligns with governance best practices
- Reduces risk in multi-developer environments

---

## 5. Controlled Use of Redundancy

### Decision
Some attributes (e.g., currency, country) are intentionally duplicated
across tables.

### Rationale
- Improves usability in associative analytics
- Simplifies expressions
- Reflects SAP analytical models
- Reduces dependency on deep joins

Redundancy is **designed**, not accidental.

---

## 6. Calendar as a First-Class Dimension

### Decision
A governed **Fiscal Calendar** is generated in the script,
not loaded from source files.

### Rationale
- Ensures consistent time logic
- Enables fiscal and rolling KPIs
- Avoids source dependency
- Centralizes date intelligence

---

## 7. FX Conversion Strategy

### Decision
Currency conversion is:
- Performed dynamically in Qlik
- Based on monthly average FX rates
- Standardized to USD

### Rationale
- Allows flexible reporting currency
- Enables scenario comparison
- Avoids data duplication
- Matches executive reporting needs

---

## 8. Consolidation Logic

### Decision
Holding-level consolidation is calculated **in the semantic layer**,
not pre-aggregated.

### Rationale
- Preserves drill-down capability
- Enables dynamic inclusion/exclusion
- Supports what-if analysis
- Reflects modern analytics patterns

---

## 9. Scenario Handling (PRE / POST)

### Decision
PRE and POST scenarios are stored in the **same fact table**
and differentiated by a `scenario` field.

### Rationale
- Simplifies KPI definitions
- Enables direct comparison
- Reduces script complexity
- Avoids duplicated models

---

## 10. Error Prevention and Data Quality

### Decision
The script includes:
- Null handling
- Explicit field naming
- Standardized formats

### Rationale
- Prevents broken associations
- Improves reload stability
- Makes issues visible early
- Supports long-term maintainability

---

## 11. Performance Considerations

### Decision
- Minimal joins on large tables
- Aggregations pushed to the semantic layer
- Use of Qlik-optimized loads where possible

### Rationale
- Ensures cloud scalability
- Reduces reload time
- Improves dashboard responsiveness

---

## 12. What Was Explicitly Avoided

The following were intentionally not used:

- Script-level KPI calculations
- Pre-aggregated fact tables
- Hard-coded business rules
- Tool-specific shortcuts

### Rationale
The goal is:
- Transparency
- Flexibility
- Executive trust in numbers

---

## 13. Alignment with Analytics Governance

This ETL design supports:
- Version control
- Peer review
- Clear ownership of logic
- Portfolio-grade documentation

It reinforces the project positioning as:
> **Modern analytics with cloud governance.**

---

## Final Note

The load script is not just a technical artifact.

It is a **contract between data, analytics, and decision-makers**.

Every decision favors:
- Clarity over cleverness
- Governance over shortcuts
- Insight over volume
