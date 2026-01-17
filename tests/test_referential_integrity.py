def test_company_holding_fk(company, holding):
    assert set(company.holding_id).issubset(set(holding.holding_id))

def test_company_country_fk(company, country):
    assert set(company.country_code).issubset(set(country.country_code))

def test_cost_center_company_fk(cost_center, company):
    assert set(cost_center.company_id).issubset(set(company.company_id))
