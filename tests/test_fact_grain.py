from pandas import DataFrame


def test_cash_position_grain_unique(cash_position: DataFrame):
    grain = [
        "calendar_date",
        "company_id",
        "cost_center_id",
        "scenario",
    ]
    assert not cash_position.duplicated(subset=grain).any()
