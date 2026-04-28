from scripts.extract.csv_loader import load_csv

def test_csv_loader():
    df = load_csv("data/fuel_deliveries.csv")
    assert len(df) > 0

