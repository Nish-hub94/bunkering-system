from scripts.extract.csv_loader import load_csv

def test_csv_loader():
    df = load_csv("data/vessel_logs_cleaned.csv")
    assert len(df) > 0