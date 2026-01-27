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

def test_cash_position_has_cost_center(cash_position):
    assert "cost_center_id" in cash_position.columns

def test_cash_position_no_null_keys(cash_position):
    key_fields = [
        "calendar_date",
        "company_id",
        "cost_center_id",
        "scenario",
        "cash_amount_local",
    ]

    for field in key_fields:
        assert cash_position[field].isnull().sum() == 0

def test_company_has_nine_cost_centers(cost_center):
    counts = (
        cost_center
        .groupby("company_id")["cost_center_id"]
        .nunique()
    )

    assert (counts == 9).all()

def test_fact_cost_centers_exist_in_dimension(cash_position, cost_center):
    fact_cc = set(cash_position["cost_center_id"].unique())
    dim_cc = set(cost_center["cost_center_id"].unique())

    assert fact_cc.issubset(dim_cc)

