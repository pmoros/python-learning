from datetime import datetime
import requests


def is_weekday():
    """Check if today is a weekend."""
    today = datetime.today()
    return today.weekday() < 5


def get_holidays():
    r = requests.get("http://localhost/api/holidays")
    if r.status_code == 200:
        return r.json()
    return None
