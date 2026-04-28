from unittest.mock import patch
from scripts.extract.api_loader import load_api

@patch("requests.get")
def test_api(mock_get):
    mock_get.return_value.status_code =200
    mock_get.return_value.json.return_value = [{"fuel": "MGO", "price": 500}]

    df = load_api("fake_url")

    assert len(df) == 1