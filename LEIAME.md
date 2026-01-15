# Qlik Sense Cloud – PoC de Tesouraria com Cash Pooling

## Visão Geral

Este repositório contém um **Proof of Concept (PoC)** desenvolvido em **Qlik Sense Cloud (SaaS)** que simula um **processo de Cash Pooling em uma tesouraria multinacional**.

O objetivo deste PoC é demonstrar, de ponta a ponta, como **analytics moderno em cloud** pode suportar **tomada de decisão financeira**, cobrindo:

- Ingestão de dados e ETL
- Modelagem de dados
- Visual analytics
- Aspectos de governança em ambiente cloud

Todos os dados utilizados neste projeto são **sintéticos**, porém **realistas e inspirados em estruturas financeiras do SAP S/4HANA**.

---

## Contexto de Negócio

### Cenário

A empresa simulada é um **grupo multinacional**, com operações em múltiplos países e entidades legais.  
Inicialmente, cada subsidiária gerencia sua posição de caixa de forma independente, o que resulta em:

- Excesso de liquidez em algumas empresas
- Déficit de caixa e necessidade de financiamento em outras
- Baixa visibilidade da posição de caixa consolidada do grupo

---

### Processo de Tesouraria: Cash Pooling

O PoC tem como foco a **implantação de um processo de Cash Pooling**, no qual:

- O excesso de caixa das subsidiárias é centralizado no nível da holding
- Há compensação interna entre empresas superavitárias e deficitárias
- A dependência de financiamento externo é reduzida

A solução analítica permite comparar cenários **antes e depois** da implantação do Cash Pooling, evidenciando claramente **o impacto dessa mudança de procedimento**.

---

## Objetivos de Negócio e Benchmarks

Os dashboards desenvolvidos neste PoC permitem acompanhar benchmarks importantes de tesouraria, tais como:

- Redução do saldo de caixa ocioso
- Redução do número de empresas com posição de caixa negativa
- Aumento do percentual de caixa centralizado na holding
- Melhoria da visibilidade da posição de caixa consolidada

Esses benchmarks são mensuráveis e estão explicitamente refletidos no modelo de dados e nos dashboards.

---

## Escopo do PoC

### Escopo Funcional

- Análise mensal da posição de caixa
- Consolidação multiempresa e multinacional
- Análise por centro de custo
- Comparação entre cenários pré e pós Cash Pooling

---

### Escopo Técnico

- Qlik Sense Cloud (apenas SaaS)
- Ingestão de dados via arquivos CSV
- ETL via script no Qlik Load Editor
- Modelo de dados associativo
- Dashboards interativos orientados à tomada de decisão
- Conceitos básicos de governança (spaces, ownership, estrutura)

Comparações com QlikView ou arquiteturas on-premise estão **fora do escopo**, por decisão consciente.

---

## Abordagem de Dados

- **Dados sintéticos**, criados exclusivamente para fins demonstrativos
- Granularidade mensal
- Estruturas inspiradas em conceitos do **SAP S/4HANA** (ex.: company code, centro de custo, moeda)
- Separação clara entre dados brutos, processados e dados de referência

Nenhum dado real ou confidencial é utilizado neste projeto.

---

## Estrutura do Repositório

```text
qlik-sense-cloud-cash-pooling-poc/
│
├── README.md
├── LEIAME.md
│
├── data/
│   ├── raw/               # CSVs sintéticos simulando extrações SAP
│   ├── processed/         # Conjuntos de dados transformados
│   └── reference/         # Dados mestres (empresas, países, moedas)
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
