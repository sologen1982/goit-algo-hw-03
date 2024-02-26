from datetime import datetime, timedelta


def get_upcoming_birthdays(users):

    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if days_until_birthday <= 7:
            if birthday_this_year.weekday() == 5:
                days_until_birthday += 2             
                birthday_this_year += timedelta(days=+2)
            elif birthday_this_year.weekday() == 6:
                days_until_birthday += 1             
                birthday_this_year += timedelta(days=+1)           

            upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")})

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.02.28"},
    {"name": "Jane Smith", "birthday": "1990.03.03"},
    {"name": "Papa Karla", "birthday": "1992.03.02"},
    {"name": "Mama Lena", "birthday": "1980.02.24"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
