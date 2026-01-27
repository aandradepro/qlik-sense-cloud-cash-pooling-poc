# Qlik Sense Cloud – Cash Pooling Treasury PoC
[versão pt_BR](LEIAME.md)
## Overview

This repository contains a **Proof of Concept (PoC)** built on **Qlik Sense Cloud (SaaS)** that simulates a **multinational treasury Cash Pooling process**.

The goal of this PoC is to demonstrate, end to end, how modern cloud analytics can support **financial decision-making**, covering:

- Data ingestion and ETL
- Data modeling
- Visual analytics
- Governance considerations in a cloud environment

All data used in this project is **synthetic**, but designed to be **realistic and inspired by SAP S/4HANA financial structures**.

---

## Business Context

### Scenario

The simulated company is a **multinational group** operating across multiple countries and legal entities.  
Initially, each subsidiary manages its own cash position independently, which leads to:

- Excess liquidity in some entities
- Cash deficits and financing needs in others
- Limited visibility of the group’s consolidated cash position

---

### Treasury Process: Cash Pooling

The PoC focuses on the **implementation of a Cash Pooling process**, where:

- Surplus cash from subsidiaries is centralized at the holding level
- Internal compensation between surplus and deficit entities is enabled
- Dependence on external financing is reduced

The analytics solution allows comparison of **before and after** scenarios, clearly showing the **impact of this procedural change**.

---

## Business Goals & Benchmarks

The dashboards built in this PoC allow tracking of key treasury benchmarks, such as:

- Reduction of idle cash balances
- Reduction in the number of entities with negative cash positions
- Increase in the percentage of cash centralized at holding level
- Improved visibility of consolidated cash positions

These benchmarks are measurable and explicitly reflected in the data model and dashboards.

---

## Scope of the PoC

### Functional Scope

- Monthly cash position analysis
- Multi-company and multi-country consolidation
- Analysis by cost center
- Comparison of pre- and post-Cash Pooling scenarios

### Technical Scope

- Qlik Sense Cloud (SaaS only)
- CSV-based data ingestion
- Script-based ETL using Qlik Load Editor
- Associative data model
- Interactive dashboards focused on decision-making
- Basic governance concepts (spaces, ownership, structure)

Comparisons with QlikView or on-premise architectures are intentionally **out of scope**.

### Out of Scope: Cash Pooling activities

This Proof of Concept does not execute a cash pooling process operationally (i.e., no cash movements, bank sweeps, or treasury transactions are performed).

Instead, the PoC is designed to analyze, compare, and govern the financial impact of a cash pooling decision, using PRE and POST strategic scenarios.

The focus of this project is decision analytics, providing CFO-level visibility into how liquidity, consolidation, and cash efficiency behave before and after the adoption of cash pooling, rather than implementing the operational mechanics of the process itself.

---

## Data Approach

- **Synthetic data** generated for demonstration purposes
- Monthly granularity
- Data structures inspired by **SAP S/4HANA** concepts (e.g., company code, cost center, currency)
- Clear separation between raw, processed, and reference data

No real or confidential data is used in this project.

---

## Repository Structure

```text
qlik-sense-cloud-cash-pooling-poc/
│
├── README.md
│
├── data/
│   ├── raw/               # Synthetic CSVs simulating SAP extractions
│   ├── processed/         # Transformed datasets
│   └── reference/         # Master data (companies, countries, currencies)
│
├── etl/
│   ├── load_script.qvs
│   └── etl_decisions.md
│
├── model/
│   └── data_model.md
│
├── dashboards/
│   └── cash_pooling_dashboards.md
│
├── governance/
│   └── decisions_and_tradeoffs.md
│
└── docs/
    ├── architecture.md
    └── roadmap.md
