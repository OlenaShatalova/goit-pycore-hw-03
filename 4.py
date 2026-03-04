from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list) -> list:
    today = datetime.today().date()
    upcoming = []

    for user in users:
        date_birth = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Формуємо ДН у поточному році
        try:
            birthday_this_year = date_birth.replace(year=today.year)
        except ValueError:
            # якщо 29 лютого у невисокосний рік
            birthday_this_year = datetime(today.year, 3, 1).date()

        # Якщо ДН вже минув — переносимо на наступний рік
        if birthday_this_year < today:
            try:
                birthday_this_year = date_birth.replace(year=today.year + 1)
            except ValueError:
                birthday_this_year = datetime(today.year + 1, 3, 1).date()

        # Різниця в днях
        delta = (birthday_this_year - today).days

        if 0 <= delta <= 7:
            congratulation_date = birthday_this_year

            # Якщо вихідний — переносимо на понеділок
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            })

    return upcoming

# users = [
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"},
#     {"name": "John Doe", "birthday": "1985.03.08"},
#     {"name": "Jane Smith", "birthday": "2000.02.29"}
# ]

# upcoming_birthdays = get_upcoming_birthdays(users)
# print("Список привітань на цьому тижні:", upcoming_birthdays)
