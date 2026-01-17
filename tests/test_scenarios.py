def test_pre_post_scenarios_complete(cash_position):
    expected = {"PRE", "POST"}

    scenario_check = (
        cash_position
        .groupby(["calendar_date", "company_id"])["scenario"]
        .apply(set)
    )

    assert scenario_check.apply(lambda s: expected.issubset(s)).all()
