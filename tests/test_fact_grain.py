def test_cash_position_grain_unique(cash_position):
    grain = ["calendar_date", "company_id", "scenario"]
    assert not cash_position.duplicated(subset=grain).any()
