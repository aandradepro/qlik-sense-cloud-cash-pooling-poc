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
