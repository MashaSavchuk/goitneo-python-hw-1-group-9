from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)
    today = datetime.today().date()
    one_week_later = today + timedelta(days=7)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year = today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year = today.year + 1)

        if birthday_this_year > one_week_later:
            continue
        delta_days = (birthday_this_year - today).days
        day_of_week = (today + timedelta(days=delta_days)).strftime("%A")

        if day_of_week == "Saturday" or day_of_week == "Sunday":
            day_of_week = "Monday"   
        birthdays_per_week[day_of_week].append(name)

    for day, users in birthdays_per_week.items():
        if users:
            print(f"{day}: {', '.join(users)}")

users = [
    {"name": "Nenny Luis", "birthday": datetime(1986, 10, 28)},
    {"name": "Din Blum", "birthday": datetime(1976, 2, 24)},
    {"name": "Robin Hud", "birthday": datetime(1984, 5, 12)},
    {"name": "Joe Nennon", "birthday": datetime(1988, 2, 26)},
    {"name": "Mike Lou", "birthday": datetime(1993, 2, 28)},
    {"name": "Pirs Brosnan", "birthday": datetime(1993, 3, 1)},
]
get_birthdays_per_week(users)
