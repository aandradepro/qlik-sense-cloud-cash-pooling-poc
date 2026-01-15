# Dados Crus – Arquivos CSV Sintéticos de Tesouraria

## Objetivo desta Pasta

Esta pasta contém os **arquivos CSV sintéticos crus** utilizados como entrada no PoC de Cash Pooling em Qlik Sense Cloud.

Esses arquivos simulam **extrações financeiras de um sistema ERP**, com estruturas e semântica inspiradas no **SAP S/4HANA**, sem utilização de dados reais ou confidenciais.

Os arquivos aqui presentes representam o **ponto inicial do processo de ETL**.  
Nesta etapa, **nenhuma regra de negócio, agregação ou consolidação deve ser assumida**.

---

## Princípios de Design

Os datasets crus foram desenhados seguindo os seguintes princípios:

- **Estrutura semelhante a ERP**  
  Nomes de campos e entidades refletem conceitos financeiros comuns do SAP, aumentando o realismo e a reconhecibilidade.

- **Transformação mínima**  
  Os dados são armazenados de forma próxima ao formato original de extração do sistema de origem.

- **Granularidade mensal**  
  Todos os valores financeiros estão no nível mensal, alinhados aos ciclos de reporte da tesouraria.

- **Multiempresa e multinacional**  
  Os dados suportam cenários de consolidação necessários ao processo de Cash Pooling.

- **Suporte a cenários Antes / Depois**  
  Campos permitem distinguir situações pré e pós implantação do Cash Pooling.

---

## Visão Geral dos Arquivos CSV Crus

### 1. `treasury_cash_position.csv`

**Descrição**  
Contém a posição de caixa mensal por empresa, país e centro de custo.

Este é o **principal dataset de fatos** para análise dos efeitos do Cash Pooling.

**Grão**
- Um registro por:
  - Empresa
  - País
  - Centro de Custo
  - Mês

**Principais Campos**

| Nome do Campo | Descrição |
|--------------|-----------|
| company_code | Identificador da entidade legal (Company Code no padrão SAP) |
| company_name | Nome da empresa |
| country | País de operação |
| cost_center | Identificador do centro de custo |
| fiscal_year | Ano fiscal |
| fiscal_month | Mês fiscal (1–12) |
| currency | Moeda local |
| opening_balance | Saldo de caixa no início do mês |
| cash_in | Total de entradas de caixa no mês |
| cash_out | Total de saídas de caixa no mês |
| closing_balance | Saldo de caixa no final do mês |
| pooling_scenario | Indicador `PRE_POOLING` ou `POST_POOLING` |

---

### 2. `companies.csv`

**Descrição**  
Dados mestres das entidades legais do grupo.

**Finalidade**
- Suportar a lógica de consolidação
- Definir o relacionamento entre subsidiárias e holding

**Principais Campos**

| Nome do Campo | Descrição |
|--------------|-----------|
| company_code | Código da empresa |
| company_name | Nome da empresa |
| parent_company | Código da holding ou empresa controladora |
| country | País de registro |
| local_currency | Moeda local da empresa |

---

### 3. `cost_centers.csv`

**Descrição**  
Dados mestres dos centros de custo utilizados na análise de tesouraria.

**Principais Campos**

| Nome do Campo | Descrição |
|--------------|-----------|
| cost_center | Código do centro de custo |
| cost_center_name | Descrição do centro de custo |
| company_code | Empresa proprietária |
| country | País |

---

### 4. `countries.csv`

**Descrição**  
Tabela de referência de países.

**Principais Campos**

| Nome do Campo | Descrição |
|--------------|-----------|
| country | Código ou nome do país |
| region | Região geográfica |
| reporting_currency | Moeda utilizada para reporte |

---

### 5. `currencies.csv`

**Descrição**  
Tabela de referência de moedas utilizadas no PoC.

**Principais Campos**

| Nome do Campo | Descrição |
|--------------|-----------|
| currency | Código da moeda (ex.: USD, EUR) |
| currency_name | Descrição da moeda |
| exchange_rate_to_group | Taxa de câmbio para a moeda de reporte do grupo |

---

## Relação com o Processo de ETL

- Os arquivos desta pasta são **carregados sem transformação** no Qlik Sense Cloud.
- Todas as transformações, cálculos e regras de consolidação são implementadas **na camada de ETL**.
- Nenhuma métrica derivada deve ser calculada diretamente a partir dos arquivos crus.

A lógica detalhada de transformação está documentada em:
etl/etl_decisions.md

---

## Premissas e Limitações

- Os dados são **sintéticos e simplificados**, com finalidade demonstrativa.
- As taxas de câmbio são estáticas e simplificadas.
- O calendário fiscal considera meses padrão.
- A estrutura prioriza clareza, não a complexidade total de um ambiente SAP real.

Essas premissas são **intencionais e explicitamente documentadas** para manter o foco do PoC em analytics e governança.

---

## Próximos Passos

Atividades planejadas relacionadas aos dados crus:

1. Geração dos arquivos CSV de exemplo com base nos layouts definidos  
2. Validação de chaves e relacionamentos  
3. Carga dos dados no Qlik Sense Cloud e início do scripting de ETL  

---

## Aviso Legal

Todos os datasets desta pasta são fictícios e foram criados exclusivamente para fins de portfólio e demonstração.
