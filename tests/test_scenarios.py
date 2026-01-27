def test_pre_post_scenarios_complete(cash_position):
    expected = {"PRE", "POST"}

    scenario_check = (
        cash_position
        .groupby(["calendar_date", "company_id"])["scenario"]
        .apply(set)
    )

    assert scenario_check.apply(lambda s: expected.issubset(s)).all()

def test_pre_and_post_exist_same_period(cash_position):
    scenarios = (
        cash_position
        .groupby("calendar_date")["scenario"]
        .unique()
    )

    for s in scenarios:
        assert set(s) == {"PRE", "POST"}

def test_post_cash_higher_than_pre_on_average(cash_position):
    avg_cash = (
        cash_position
        .groupby("scenario")["cash_amount_local"]
        .mean()
    )

    assert avg_cash["POST"] > avg_cash["PRE"]
