# Approach 1: Finding day number using calendar module

import calendar


def get_day_from_date(day_date, day_month, day_year):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]
    day_number = calendar.weekday(day_year, day_month, day_date)
    return days[day_number]


try:
    date_val = input("Enter date in DD-MM-YYYY format: ")
    date, month, year = map(int, date_val.split("-"))
    result = get_day_from_date(date, month, year)
    print(f'Day on {date_val} was {result}')
except ValueError:
    print("Date not in proper format!")