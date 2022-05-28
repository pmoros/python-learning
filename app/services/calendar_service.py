from datetime import datetime


def is_weekday():
    """Check if today is a weekend."""
    today = datetime.today()
    return today.weekday() < 5
