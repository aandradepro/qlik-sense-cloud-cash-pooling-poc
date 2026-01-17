# Dados Crus — Estrutura dos CSVs

Este diretório contém os **conjuntos de dados de entrada crus** utilizados no Proof of Concept de **Cash Pooling**.

Todos os dados são **sintéticos**, gerados com base em regras explícitas documentadas em  
`docs/data_generation_rules.md`.

Os arquivos CSV foram projetados para:
- Simular um **modelo de dados inspirado no SAP S/4HANA**
- Suportar **analytics governado** no Qlik Sense Cloud
- Permitir análises **ANTES vs DEPOIS (PRE / POST) do Cash Pooling**
- Garantir **reprodutibilidade e transparência** dos dados

---

## Propósito do Diretório

A camada `/data/raw` representa a **camada de ingestão** do pipeline analítico:

- Sem transformações
- Sem agregações
- Sem conversão de moeda
- Sem regras de negócio aplicadas

Toda a lógica de negócio e cálculos são aplicados **dentro do Qlik Sense**.

---

## Visão Geral dos Arquivos CSV

| Arquivo | Tipo | Descrição |
|---|---|---|
| `holding.csv` | Dimensão | Estrutura de holding para consolidação |
| `company.csv` | Dimensão | Cadastro das empresas (Company Code) |
| `country.csv` | Dimensão | País e moeda local |
| `cost_center.csv` | Dimensão | Centros de custo por empresa |
| `currency.csv` | Dimensão | Cadastro de moedas |
| `exchange_rate.csv` | Fato (auxiliar) | Taxas de câmbio mensais para USD |
| `cash_position.csv` | **Fato (principal)** | Posição de caixa mensal (PRE / POST) |

---

## 1. `holding.csv`

**Granularidade:** Uma linha por holding.

| Campo | Tipo | Descrição |
|---|---|---|
| holding_id | TEXTO | Identificador da holding (PK) |
| holding_name | TEXTO | Nome da holding |
| reporting_currency | TEXTO | Moeda de reporte do grupo (USD) |

---

## 2. `company.csv`

**Granularidade:** Uma linha por empresa.

| Campo | Tipo | Descrição |
|---|---|---|
| company_id | TEXTO | Identificador da empresa (PK) |
| company_name | TEXTO | Nome da empresa |
| holding_id | TEXTO | Identificador da holding (FK) |
| country_code | TEXTO | Código do país (FK) |
| local_currency | TEXTO | Moeda local da empresa |
| company_type | TEXTO | Industrial / Serviços (opcional) |

> Nota: Algumas redundâncias (ex.: moeda local) são intencionais e refletem
> práticas comuns em modelos SAP.

---

## 3. `country.csv`

**Granularidade:** Uma linha por país.

| Campo | Tipo | Descrição |
|---|---|---|
| country_code | TEXTO | Código do país (PK) |
| country_name | TEXTO | Nome do país |
| currency_code | TEXTO | Moeda local |
| region | TEXTO | Região geográfica |

---

## 4. `cost_center.csv`

**Granularidade:** Uma linha por centro de custo **por empresa**.

Cada empresa possui **9 centros de custo**:
- 3 Operacionais
- 3 Administrativos
- 3 Comerciais

| Campo | Tipo | Descrição |
|---|---|---|
| cost_center_id | TEXTO | Código do centro de custo |
| cost_center_type | TEXTO | OP / AD / CO |
| cost_center_name | TEXTO | Descrição do centro de custo |
| company_id | TEXTO | Identificador da empresa (FK) |

> Centros de custo **não fazem parte da granularidade do fato**.  
> São utilizados para filtros, drill-down e governança.

---

## 5. `currency.csv`

**Granularidade:** Uma linha por moeda.

| Campo | Tipo | Descrição |
|---|---|---|
| currency_code | TEXTO | Código da moeda (PK) |
| currency_name | TEXTO | Nome da moeda |

---

## 6. `exchange_rate.csv`

**Granularidade:** Uma linha por moeda **por mês**.

Contém **taxas médias mensais** para conversão em USD.

| Campo | Tipo | Descrição |
|---|---|---|
| calendar_date | DATA | Data de fechamento do mês |
| fiscal_year | INTEIRO | Ano fiscal |
| fiscal_month | INTEIRO | Mês fiscal |
| from_currency | TEXTO | Moeda de origem |
| to_currency | TEXTO | Moeda de destino (USD) |
| fx_rate | DECIMAL | Taxa de câmbio |

Regras:
- A mesma taxa se aplica a todas as empresas no mesmo mês
- A taxa USD → USD é sempre 1,0

---

## 7. `cash_position.csv` (Fato Principal)

**Granularidade:**  
**Empresa + Mês + Cenário**

Esta é a **tabela fato central** do PoC.

| Campo | Tipo | Descrição |
|---|---|---|
| calendar_date | DATA | Data de fechamento do mês |
| fiscal_year | INTEIRO | Ano fiscal |
| fiscal_month | INTEIRO | Mês fiscal |
| scenario | TEXTO | PRE ou POST |
| holding_id | TEXTO | Identificador da holding |
| company_id | TEXTO | Identificador da empresa |
| country_code | TEXTO | Código do país |
| local_currency | TEXTO | Moeda local |
| cash_amount_local | DECIMAL | Saldo de caixa (moeda local) |

Importante:
- Os valores são sempre **positivos**
- Nenhuma conversão de moeda é aplicada neste arquivo
- Os cenários PRE e POST coexistem na mesma tabela

---

## Observações de Modelagem

- O modelo utiliza **redundância controlada**
- Não existem dados transacionais
- Todas as métricas (FX, consolidação, KPIs) são calculadas no Qlik
- A estrutura prioriza **clareza, performance e análise executiva**

---

## Aviso de Uso

Esses dados são:
- Totalmente sintéticos
- Criados exclusivamente para demonstrações analíticas
- Não devem ser usados para fins contábeis ou regulatórios

---

## Próximos Passos

Após o carregamento no Qlik Sense Cloud:
1. Aplicar transformações governadas
2. Implementar conversão de moeda
3. Executar consolidação por holding
4. Construir dashboards executivos
