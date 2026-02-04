# Calendar
Type: Drill-down
*Field / Label*
fiscal_year / Year
fiscal_month / Month
date / Day

# Company
Type: Single
Field: company_name

# Cost Center
Type: Single
Field: cost_center_name

# Country
Type: Single
Field: country_name

# FX Exposure Ststus
Type: Single
Field: =If( cash_currency = reporting_currency, 'Not FX Exposed', 'FX Exposed' )

# Holding
Type: Single
Field: holding_name

# Scenario
Type: Single
Field: scenario