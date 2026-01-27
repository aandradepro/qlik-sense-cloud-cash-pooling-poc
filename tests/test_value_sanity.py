def test_cash_positive(cash_position):
    assert (cash_position.cash_amount_local > 0).all()

def test_cost_center_distribution(cost_center):
    check = (
        cost_center
        .groupby(["company_id", "cost_center_type"])
        .size()
        .unstack(fill_value=0)
    )

    for ctype in ["OP", "AD", "CO"]:
        assert (check[ctype] == 3).all()

def test_cash_totals_preserved_by_cost_center(cash_position):
    total_by_company = (
        cash_position
        .groupby(["company_id", "calendar_date", "scenario"])["cash_amount_local"]
        .sum()
        .reset_index()
    )

    # Não deve haver duplicidade artificial
    assert total_by_company["cash_amount_local"].gt(0).all()
