# Dashboard Decisions – Cash Pooling PoC (Qlik Sense Cloud) [en_US]

## Purpose of This Document

This document explains the **design decisions behind the dashboards** created for the Cash Pooling Proof of Concept in **Qlik Sense Cloud**.

The goal is not to document *how to build charts*, but to explain:
- **Why certain views were chosen**
- **Which business questions each dashboard answers**
- **How governance and clarity were prioritized over visual complexity**

This document is part of a **professional analytics portfolio** and reflects an executive-oriented mindset.

---

## Target Audience

The dashboards are designed primarily for:

- CFO
- Group Treasurer
- Head of Finance
- Senior Finance Business Partners

Secondary audience:
- Analytics and BI leaders evaluating the solution architecture

---

## Core Design Principles

### 1. Decision-Driven Design

**Decision**  
> Every dashboard must answer at least one concrete business question.

**Rationale**
- Dashboards exist to support decisions, not exploration without purpose
- Especially in treasury, clarity and trust are critical

---

### 2. Governance Over Visual Sophistication

**Decision**  
> Prefer simple, explainable visuals over advanced or exotic chart types.

**Rationale**
- Financial stakeholders prioritize correctness and traceability
- Overly complex visuals reduce adoption and trust

---

### 3. Minimal Cognitive Load

**Decision**  
> Limit each dashboard to a small number of key metrics and visuals.

**Rationale**
- Executives scan dashboards, they do not study them
- Key insights must be immediately visible

---

## Dashboard Structure Overview

The PoC includes **one primary executive dashboard**, optionally expandable later.

### Dashboard 1 – Cash Pooling Executive Overview

**Primary Question**
> Did Cash Pooling reduce idle cash and improve treasury efficiency?

---

## Dashboard 1 – Design Decisions

### 1. KPI Section (Top of the Dashboard)

**KPIs Displayed**
- Average Cash Balance (Group Currency)
- Cash Reduction (Absolute)
- Cash Reduction (%)
- Net Cash Movement

**Decision**  
> Place KPIs at the top, without requiring filters or interaction.

**Rationale**
- Immediate executive visibility
- Reduces time-to-insight
- Aligns with CFO-level consumption patterns

---

### 2. Before vs After Comparison

**Visual Choice**
- Side-by-side bar chart or grouped bar chart

**Dimensions**
- Pooling Scenario (PRE vs POST)

**Measures**
- Average Monthly Cash Balance (Group Currency)

**Decision**  
> Use direct visual comparison instead of delta-only charts.

**Rationale**
- Executives want to see *both states*
- Deltas without context reduce interpretability

---

### 3. Time Evolution View

**Visual Choice**
- Line chart

**Dimensions**
- Fiscal Year-Month

**Measures**
- Average Monthly Cash Balance (Group Currency)

**Decision**  
> Show trend over time even if executives focus on summary KPIs.

**Rationale**
- Builds confidence in the numbers
- Reveals seasonality and anomalies
- Supports follow-up questions

---

### 4. Consolidation Perspective

**Visual Choice**
- Bar chart or table

**Dimensions**
- Holding Company
- Company (drill-down)

**Measures**
- Average Monthly Cash Balance
- Cash Reduction

**Decision**  
> Enable consolidated and entity-level views in the same dashboard.

**Rationale**
- Reflects real treasury governance models
- Allows drill-down without changing dashboards
- Demonstrates modeling robustness

---

## Filters and Interaction Design

### Global Filters

- Fiscal Year
- Country
- Holding Company

**Decision**  
> Limit filters to organizational and temporal dimensions.

**Rationale**
- Prevents over-filtering
- Keeps narrative coherent
- Reduces risk of misinterpretation

---

### Excluded Filters (Intentional)

- Currency
- Scenario (PRE/POST)

**Decision**  
> Do not expose scenario selection as a filter.

**Rationale**
- Scenario comparison is the core narrative
- Allowing users to remove one scenario breaks the story

---

## Benchmark Representation

### Benchmarks Used

- Absolute reduction in average cash
- Percentage reduction after Cash Pooling

**Decision**  
> Benchmarks are visualized, not hard-coded as targets.

**Rationale**
- Targets vary by company
- Executives prefer contextual judgment
- Avoids false precision

---

## Validation and Trust Indicators

### Data Quality Indicator

- Balance check flag available for internal validation

**Decision**  
> Do not expose technical validation flags in executive dashboards.

**Rationale**
- Executives care about trust, not mechanics
- Validation belongs to development and QA views

---

## What Is Explicitly Out of Scope

- Intraday cash positioning
- Bank account–level analysis
- Forecasting and scenario simulation

**Decision**  
> Keep scope intentionally limited.

**Rationale**
- PoC focus is impact visualization, not full treasury system replacement
- Depth can be added incrementally

---

## Alignment with ETL Decisions

The dashboard design directly reflects ETL choices:

| ETL Decision | Dashboard Impact |
|-------------|------------------|
| Monthly grain | Monthly trend views |
| Scenario attribute | Before vs After visuals |
| Group currency conversion | Executive-ready KPIs |
| Hierarchical consolidation | Drill-down capability |

---

## Final Notes

This dashboard design emphasizes:

- Business impact over technical showcase
- Explainability over complexity
- Governance over visual experimentation

The result is a dashboard that:
- Can be confidently shown to executives
- Is defensible in technical reviews
- Clearly demonstrates senior analytics thinking
******************************************************************************
# Decisões de Dashboard – PoC de Cash Pooling (Qlik Sense Cloud) [pt_BR]

## Objetivo deste Documento

Este documento descreve as **decisões de design adotadas na construção dos dashboards** do Proof of Concept de Cash Pooling em **Qlik Sense Cloud**.

O objetivo **não é** explicar como construir gráficos, mas sim documentar:
- **Por que determinados painéis e visões foram escolhidos**
- **Quais perguntas de negócio cada dashboard responde**
- **Como governança, clareza e tomada de decisão orientaram o design**

Este documento faz parte de um **portfólio profissional em analytics** e reflete uma abordagem orientada a executivos.

---

## Público-Alvo

Os dashboards foram desenhados principalmente para:

- CFO
- Tesoureiro Corporativo (Group Treasurer)
- Head de Finanças
- Finance Business Partners Sênior

Público secundário:
- Líderes de BI e Analytics avaliando arquitetura e governança da solução

---

## Princípios Fundamentais de Design

### 1. Design Orientado à Decisão

**Decisão**  
> Todo dashboard deve responder a pelo menos uma pergunta clara de negócio.

**Justificativa**
- Dashboards existem para suportar decisões, não apenas exploração de dados
- Em tesouraria, clareza e confiança são essenciais

---

### 2. Governança Acima de Sofisticação Visual

**Decisão**  
> Priorizar visuais simples e facilmente explicáveis em vez de gráficos complexos ou pouco convencionais.

**Justificativa**
- Stakeholders financeiros valorizam correção e rastreabilidade
- Visuais excessivamente complexos reduzem adoção e confiança

---

### 3. Baixa Carga Cognitiva

**Decisão**  
> Limitar cada dashboard a um conjunto reduzido de métricas e visões-chave.

**Justificativa**
- Executivos analisam dashboards rapidamente
- Os principais insights devem ser imediatos

---

## Visão Geral da Estrutura de Dashboards

O PoC inclui **um dashboard executivo principal**, com possibilidade de expansão futura.

### Dashboard 1 – Visão Executiva de Cash Pooling

**Pergunta Principal**
> O Cash Pooling reduziu o caixa ocioso e aumentou a eficiência da tesouraria?

---

## Dashboard 1 – Decisões de Design

### 1. Seção de KPIs (Topo do Dashboard)

**KPIs Exibidos**
- Saldo Médio de Caixa (Moeda do Grupo)
- Redução de Caixa (Valor Absoluto)
- Redução de Caixa (%)
- Movimentação Líquida de Caixa

**Decisão**  
> Posicionar KPIs no topo, sem necessidade de filtros ou interações.

**Justificativa**
- Visibilidade imediata para executivos
- Redução do tempo até o insight
- Alinhamento com o padrão de consumo de CFOs

---

### 2. Comparação Antes vs Depois

**Escolha de Visual**
- Gráfico de barras agrupadas ou lado a lado

**Dimensão**
- Cenário de Pooling (ANTES vs DEPOIS)

**Métrica**
- Saldo Médio Mensal de Caixa (Moeda do Grupo)

**Decisão**  
> Utilizar comparação visual direta em vez de apenas mostrar variações (delta).

**Justificativa**
- Executivos precisam enxergar os dois estados
- Variações sem contexto reduzem entendimento

---

### 3. Evolução Temporal

**Escolha de Visual**
- Gráfico de linha

**Dimensão**
- Ano-Mês Fiscal

**Métrica**
- Saldo Médio Mensal de Caixa (Moeda do Grupo)

**Decisão**  
> Incluir visão temporal mesmo que o foco seja executivo.

**Justificativa**
- Aumenta a confiança nos números
- Evidencia sazonalidade e anomalias
- Antecipação de questionamentos naturais

---

### 4. Visão de Consolidação

**Escolha de Visual**
- Gráfico de barras ou tabela

**Dimensões**
- Holding
- Empresa (com drill-down)

**Métricas**
- Saldo Médio Mensal de Caixa
- Redução de Caixa

**Decisão**  
> Permitir visão consolidada e por entidade no mesmo dashboard.

**Justificativa**
- Reflete modelos reais de governança em tesouraria
- Drill-down sem troca de dashboard
- Demonstra robustez do modelo de dados

---

## Filtros e Interação

### Filtros Globais

- Ano Fiscal
- País
- Holding

**Decisão**  
> Restringir filtros a dimensões organizacionais e temporais.

**Justificativa**
- Evita excesso de filtragem
- Mantém a narrativa consistente
- Reduz risco de interpretação incorreta

---

### Filtros Excluídos (Decisão Intencional)

- Moeda
- Cenário (ANTES / DEPOIS)

**Decisão**  
> Não expor o cenário como filtro selecionável.

**Justificativa**
- A comparação de cenários é o núcleo da narrativa
- Remover um cenário quebra a lógica do dashboard

---

## Representação de Benchmark

### Benchmarks Utilizados

- Redução absoluta do saldo médio de caixa
- Redução percentual após Cash Pooling

**Decisão**  
> Benchmarks são apresentados visualmente, não como metas fixas.

**Justificativa**
- Metas variam por empresa e contexto
- Executivos preferem julgamento contextual
- Evita falsa precisão

---

## Indicadores de Confiança e Validação

### Qualidade de Dados

- Flags de validação disponíveis para uso técnico interno

**Decisão**  
> Não expor indicadores técnicos de validação em dashboards executivos.

**Justificativa**
- Executivos confiam no resultado, não no mecanismo
- Validação pertence às camadas técnica e de QA

---

## Escopo Explicitamente Fora do PoC

- Posição de caixa intradiária
- Análise por conta bancária
- Forecast e simulações avançadas

**Decisão**  
> Manter o escopo propositalmente controlado.

**Justificativa**
- O PoC visa demonstrar impacto, não substituir sistemas de tesouraria
- Aprofundamentos podem ser adicionados futuramente

---

## Alinhamento com Decisões de ETL

O design dos dashboards reflete diretamente as decisões de ETL:

| Decisão de ETL | Impacto no Dashboard |
|---------------|----------------------|
| Granularidade mensal | Visões temporais mensais |
| Atributo de cenário | Comparação Antes vs Depois |
| Conversão para moeda do grupo | KPIs prontos para executivos |
| Consolidação hierárquica | Capacidade de drill-down |

---

## Considerações Finais

Este design de dashboard prioriza:

- Impacto de negócio sobre exibição técnica
- Clareza sobre complexidade
- Governança sobre experimentação visual

O resultado é um dashboard que:
- Pode ser apresentado com segurança a executivos
- É defensável em revisões técnicas
- Demonstra claramente senioridade em analytics moderno
