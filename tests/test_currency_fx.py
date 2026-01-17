def test_cash_currency_exists(cash_position, currency):
    assert set(cash_position.local_currency).issubset(
        set(currency.currency_code)
    )

def test_fx_rate_positive(exchange_rate):
    assert (exchange_rate.fx_rate > 0).all()

def test_usd_fx_is_one(exchange_rate):
    usd = exchange_rate[exchange_rate.from_currency == "USD"]
    assert (usd.fx_rate == 1.0).all()

def test_fx_coverage(cash_position, exchange_rate):
    required = (
        cash_position[["calendar_date", "local_currency"]]
        .drop_duplicates()
        .rename(columns={"local_currency": "from_currency"})
    )

    merged = required.merge(
        exchange_rate,
        on=["calendar_date", "from_currency"],
        how="left"
    )

    assert not merged.fx_rate.isnull().any()
