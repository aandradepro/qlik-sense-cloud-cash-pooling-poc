# Average Daily Cash
Expression: Avg( Aggr( Sum(cash_amount), date ) )
Number formatting: Number
Formatting: Simple [1,000.12]

# Cash Amount [$DC]
Expression: Sum(cash_amount)
Description: Cash Amount in document currency
Label expression: =''
Number formatting: Money
Format pattern: $ #,##0.00;-$ #,##0.00

# Cash Amount [$RC]
Expression: Sum(reporting_amount)
Description: Cash Amount in reporting currency
Label expression: =''
Number formatting: Money
Format pattern: $ #,##0.00;-$ #,##0.00

# Delta Pooling [%]
Expression: ( Sum( {<scenario={'POST'}>} cash_amount ) / Sum( {<scenario={'PRE'}>} cash_amount ) ) - 1
Number formatting: Number
Formatting: Simple [12.3%]

# Delta Pooling [$DC]
Expression: ( Sum( {<scenario={'POST'}>} cash_amount ) / Sum( {<scenario={'PRE'}>} cash_amount ) ) - 1
Number formatting: Auto

# Total Cash - POST [$DC]
Expression: Sum( {<scenario={'POST'}>} cash_amount )
Number formatting: Money
Format pattern: $ #,##0.00;-$ #,##0.00

# Total Cash - POST [$RC]
Expression: Sum( {<scenario={'POST'}>} reporting_amount )
Number formatting: Money
Format pattern: $ #,##0.00;-$ #,##0.00

# Total Cash - PRE [$DC]
Expression: Sum( {<scenario={'PRE'}>} cash_amount )
Number formatting: Money
Format pattern: $ #,##0.00;-$ #,##0.00

# Total Cash - PRE [$RC]
Expression: Sum( {<scenario={'PRE'}>} reporting_amount )
Number formatting: Money
Format pattern: $ #,##0.00;-$ #,##0.00