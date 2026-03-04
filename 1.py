from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - input_date
    except ValueError:
        print(f"{date} не відповідає формату 'YYYY-MM-DD'")
        return None
    else:
        return delta.days

# print(get_days_from_today("2026/2/28"))
# print(get_days_from_today("2026-3-21"))
