# ETL Decisions – Cash Pooling PoC (Qlik Sense Cloud) [en_US]

## Purpose of This Document

This document describes **all ETL (Extract, Transform, Load) decisions** adopted in the Cash Pooling Proof of Concept developed using **Qlik Sense Cloud**.

The focus is not only on *how* data was transformed, but primarily on **why each decision was made**, considering:
- Modern analytics best practices
- Data governance in cloud environments
- Scalability and maintainability
- Clarity for both technical and business stakeholders

This document is an integral part of a **professional analytics portfolio** and is intentionally written as such.

---

## ETL Scope

The ETL process covers:

- Loading **raw (crude) data** from CSV files
- Building a **governed analytical data model**
- Implementing financial consolidation rules
- Preparing data for Cash Pooling impact analysis
- Supporting *Before vs After* comparative analysis

---

## ETL Architecture Overview

### General Approach

An **in-tool ETL approach** was adopted, using exclusively:

- Qlik Sense Cloud
- Qlik Load Script

**Decision**  
> No external ETL tools are used in this PoC.

**Rationale**
- The goal is to demonstrate strong command of Qlik Sense Cloud
- It reduces operational complexity
- It reflects real-world PoC and MVP scenarios in cloud analytics

---

## Logical Data Layers

Although data is physically stored as CSV files, the ETL follows a **logical layered architecture**:

### 1. Raw Layer (Crude Data)

**Source**
data/raw/*.csv
**Characteristics**
- Data is loaded with minimal transformation
- Original structure and granularity are preserved
- No derived metrics are calculated at this stage

**Decision**  
> No cleansing or enrichment is performed in the raw layer.

**Rationale**
- Improves traceability
- Allows full reload and reprocessing
- Aligns with data lake / lakehouse principles

---

### 2. Transformation Layer

**Responsibilities**
- Key standardization
- Calendar creation
- Currency handling
- Master data enrichment
- Preparation for financial consolidation

**Decision**  
> Centralize business rules in this layer.

**Rationale**
- Prevents logic duplication in dashboards
- Simplifies maintenance and evolution
- Ensures analytical consistency

---

### 3. Analytical Layer (Final Model)

**Characteristics**
- Logical star schema
- Clearly defined fact and dimension tables
- Metrics ready for consumption

**Decision**  
> Clearly separate financial facts from organizational dimensions.

**Rationale**
- Improves performance
- Enhances model readability
- Reflects standard corporate BI practices

---

## Key Modeling Decisions

### Fact Table Grain

**Main Fact Table**
- `Fact_Cash_Position`

**Grain**
- Company
- Country
- Cost Center
- Month
- Scenario (Pre / Post Pooling)

**Decision**  
> Maintain monthly granularity.

**Rationale**
- Aligned with real treasury processes
- Avoids unnecessary noise
- Suitable for executive-level analysis

---

## Cash Pooling Representation

### Process Modeling

Cash Pooling is represented through the field:
pooling_scenario
Possible values:
- `PRE_POOLING`
- `POST_POOLING`

**Decision**  
> Model Cash Pooling as an analytical attribute rather than separate datasets.

**Rationale**
- Enables direct comparisons
- Reduces model complexity
- Supports flexible filtering and slicing

---

## Financial Consolidation

### Intercompany Consolidation

Consolidation is enabled through:

- Company-to-holding hierarchy
- `parent_company` field in the company dimension

**Decision**  
> Implement consolidation via hierarchy instead of pre-aggregated data.

**Rationale**
- Supports both consolidated and standalone views
- Reflects multinational corporate structures
- Preserves analytical detail

---

## Currency Handling

### Conversion Strategy

- Monetary values are stored in local currency
- Conversion to group reporting currency is performed using reference tables

**Decision**  
> Perform currency conversion during ETL, not at the front-end.

**Rationale**
- Improves dashboard performance
- Avoids repeated calculations
- Ensures metric consistency

---

## Time and Calendar

### Fiscal Calendar

A dedicated calendar is derived from:
- Fiscal year
- Fiscal month

**Decision**  
> Use an explicit calendar table in the data model.

**Rationale**
- Simplifies time-based analysis
- Enables MoM and YoY comparisons
- Is standard practice in enterprise analytics

---

## Derived Metrics

### Examples of Metrics Created in ETL

- Average monthly cash balance
- Cash variation
- Idle cash reduction
- Cash Pooling impact percentage

**Decision**  
> Create critical metrics in ETL, not only in dashboards.

**Rationale**
- Metric governance
- Reusability across analyses
- Reduced risk of inconsistent interpretations

---

## Governance and Best Practices

### Naming Conventions

- Tables: `Dim_*`, `Fact_*`
- Fields: snake_case, descriptive names

### Documentation

- All relevant decisions documented in this file
- Assumptions explicitly stated

**Decision**  
> Treat documentation as part of the delivered product.

**Rationale**
- Differentiates senior solutions from basic prototypes
- Simplifies onboarding and handover
- Reinforces governance maturity

---

## Known Limitations

- Synthetic data only
- Simplified exchange rate logic
- No complex tax or regulatory scenarios

These limitations are **intentional and controlled**, keeping the focus on analytics design.

---

## Next Steps

1. Implement the Qlik Sense Cloud load script
2. Validate the data model
3. Build analytical dashboards
4. Document visualization and UX decisions

---

## Final Note

This ETL was designed to demonstrate **architectural thinking**, not just technical execution.

Its purpose is to highlight the ability to:
- Make informed decisions
- Justify them from both technical and business perspectives
- Apply best practices in modern cloud analytics


*************************************************************************
# ETL Decisions – Cash Pooling PoC (Qlik Sense Cloud) [ptBR]

## Objetivo deste Documento

Este documento descreve **todas as decisões de ETL (Extract, Transform, Load)** adotadas no Proof of Concept de Cash Pooling desenvolvido em **Qlik Sense Cloud**.

O foco não é apenas *como* os dados foram transformados, mas **por que cada decisão foi tomada**, considerando:
- Boas práticas de analytics moderno
- Governança de dados em ambiente cloud
- Escalabilidade e manutenibilidade
- Clareza para stakeholders técnicos e de negócio

Este documento faz parte do **portfólio profissional** e deve ser lido como tal.

---

## Escopo do ETL

O processo de ETL cobre:

- Carga de **dados crus** a partir de arquivos CSV
- Criação de um **modelo analítico governado**
- Implementação de regras de consolidação financeira
- Preparação dos dados para análise do impacto do **Cash Pooling**
- Suporte a análises comparativas *Antes vs Depois*

---

## Visão Geral da Arquitetura de ETL

### Abordagem Geral

Foi adotada uma abordagem de ETL **in-tool**, utilizando exclusivamente:

- Qlik Sense Cloud
- Qlik Script (Load Script)

**Decisão**
> Não utilizar ferramentas externas de ETL neste PoC.

**Justificativa**
- O objetivo é demonstrar domínio da ferramenta Qlik Sense Cloud
- Reduz complexidade operacional
- É coerente com cenários reais de PoCs e MVPs em cloud analytics

---

## Camadas Lógicas de Dados

Embora fisicamente os dados estejam em arquivos CSV, o ETL segue uma **separação lógica em camadas**:

### 1. Camada Raw (Dados Crus)

**Origem**
data/raw/*.csv

**Características**
- Dados carregados com transformação mínima
- Preservação de nomenclatura e granularidade de origem
- Sem cálculos de métricas derivadas

**Decisão**
> Não realizar limpeza ou enriquecimento nesta camada.

**Justificativa**
- Facilita rastreabilidade
- Permite reprocessamento completo
- Alinha-se a práticas de data lake / lakehouse

---

### 2. Camada de Transformação

**Responsabilidades**
- Padronização de chaves
- Criação de calendários
- Tratamento de moedas
- Enriquecimento com dados mestres
- Preparação para consolidação

**Decisão**
> Centralizar regras de negócio nesta camada.

**Justificativa**
- Evita duplicação de lógica nos dashboards
- Facilita manutenção e evolução
- Garante consistência analítica

---

### 3. Camada Analítica (Modelo Final)

**Características**
- Modelo estrela lógico
- Tabelas de fatos e dimensões bem definidas
- Métricas prontas para consumo

**Decisão**
> Separar claramente fatos financeiros de dimensões organizacionais.

**Justificativa**
- Melhora performance
- Facilita entendimento por analistas
- É padrão em ambientes corporativos de BI

---

## Decisões-Chave de Modelagem

### Grão da Tabela Fato

**Fato Principal**
- `Fact_Cash_Position`

**Grão**
- Empresa
- País
- Centro de Custo
- Mês
- Cenário (Pre / Post Pooling)

**Decisão**
> Manter granularidade mensal.

**Justificativa**
- Alinhado a processos reais de tesouraria
- Evita ruído excessivo
- Compatível com análises executivas

---

## Tratamento de Cash Pooling

### Representação do Processo

O Cash Pooling é representado por meio do campo:
pooling_scenario

Valores possíveis:
- `PRE_POOLING`
- `POST_POOLING`

**Decisão**
> Modelar Cash Pooling como um atributo analítico, não como tabelas separadas.

**Justificativa**
- Facilita comparações diretas
- Reduz complexidade do modelo
- Permite filtros e análises flexíveis

---

## Consolidação Financeira

### Consolidação entre Empresas

A consolidação é suportada via:

- Hierarquia empresa → holding
- Campo `parent_company` na dimensão de empresas

**Decisão**
> Implementar consolidação via hierarquia, não via pré-agregação.

**Justificativa**
- Permite análises tanto consolidadas quanto individuais
- Reflete práticas reais de grupos multinacionais
- Evita perda de detalhe

---

## Tratamento de Moedas

### Estratégia de Conversão

- Valores mantidos em moeda local
- Conversão para moeda do grupo via tabela de referência

**Decisão**
> Converter valores no ETL, não no front-end.

**Justificativa**
- Melhora performance dos dashboards
- Evita cálculos repetidos
- Garante consistência nos resultados

---

## Calendário e Tempo

### Calendário Fiscal

Foi criado um calendário derivado a partir de:
- Ano fiscal
- Mês fiscal

**Decisão**
> Utilizar calendário explícito no modelo.

**Justificativa**
- Facilita análises temporais
- Permite comparações YoY e MoM
- É prática padrão em analytics corporativo

---

## Métricas Derivadas

### Exemplos de Métricas Criadas no ETL

- Saldo médio mensal
- Variação de caixa
- Redução de saldo ocioso
- Impacto percentual do Cash Pooling

**Decisão**
> Criar métricas críticas no ETL, não apenas no dashboard.

**Justificativa**
- Governança de métricas
- Reutilização consistente
- Redução de risco de interpretações divergentes

---

## Governança e Boas Práticas

### Nomenclatura

- Tabelas: `Dim_*`, `Fact_*`
- Campos: snake_case, nomes descritivos

### Documentação

- Todas as decisões relevantes documentadas neste arquivo
- Premissas explicitadas

**Decisão**
> Tratar documentação como parte do produto.

**Justificativa**
- Diferencia soluções seniores de protótipos básicos
- Facilita onboarding e handover
- Reforça maturidade em governança

---

## Limitações Conhecidas

- Dados sintéticos
- Regras simplificadas de câmbio
- Ausência de exceções fiscais complexas

Essas limitações são **intencionais** e **controladas**, visando foco analítico.

---

## Próximos Passos

1. Implementação do script de carga no Qlik Sense Cloud
2. Validação do modelo de dados
3. Criação dos dashboards analíticos
4. Documentação das decisões de visualização

---

## Nota Final

Este ETL foi projetado para demonstrar **pensamento arquitetural**, não apenas execução técnica.

O objetivo é evidenciar capacidade de:
- Tomada de decisão
- Justificativa técnica e de negócio
- Aplicação de boas práticas em cloud analytics
