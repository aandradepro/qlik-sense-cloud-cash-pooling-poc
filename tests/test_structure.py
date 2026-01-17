def test_holding_pk_unique(holding):
    assert not holding.holding_id.duplicated().any()

def test_company_pk_unique(company):
    assert not company.company_id.duplicated().any()

def test_country_pk_unique(country):
    assert not country.country_code.duplicated().any()

def test_currency_pk_unique(currency):
    assert not currency.currency_code.duplicated().any()

def test_cost_center_pk_unique(cost_center):
    assert not cost_center.cost_center_id.duplicated().any()
