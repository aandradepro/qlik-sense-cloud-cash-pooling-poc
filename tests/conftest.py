import pytest
import pandas as pd
from pathlib import Path

# Path absoluto baseado na localização deste arquivo
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw"

@pytest.fixture(scope="session")
def holding():
    return pd.read_csv(DATA_PATH / "holding.csv")

@pytest.fixture(scope="session")
def company():
    return pd.read_csv(DATA_PATH / "company.csv")

@pytest.fixture(scope="session")
def country():
    return pd.read_csv(DATA_PATH / "country.csv")

@pytest.fixture(scope="session")
def currency():
    return pd.read_csv(DATA_PATH / "currency.csv")

@pytest.fixture(scope="session")
def cost_center():
    return pd.read_csv(DATA_PATH / "cost_center.csv")

@pytest.fixture(scope="session")
def exchange_rate():
    return pd.read_csv(
        DATA_PATH / "exchange_rate.csv",
        parse_dates=["calendar_date"]
    )

@pytest.fixture(scope="session")
def cash_position():
    return pd.read_csv(
        DATA_PATH / "cash_position.csv",
        parse_dates=["calendar_date"]
    )
