from datetime import date, datetime


def get_birthdays_per_week(users):
    today = date.today()
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    birthdays = {day: [] for day in weekdays}

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        if birthday_this_year < today:
            birthday_next_year = birthday_this_year.replace(year=today.year+1)
            day_of_week = birthday_next_year.weekday()
        else:
            day_of_week = birthday_this_year.weekday()

        days_until_birthday = (birthday_this_year - today).days
        is_birthday_soon = (
            0 <= days_until_birthday <= 6 or
            (birthday_this_year < today and
                (0 <= (birthday_next_year - today).days and
                    (birthday_next_year - today).days <= 6))
            )
        if is_birthday_soon:
            if day_of_week >= 5:
                day_of_week = 0
            birthdays[weekdays[day_of_week]].append(user["name"])

    return {day: names for day, names in birthdays.items() if names}


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
