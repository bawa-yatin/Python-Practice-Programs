# Find the day of the week from given date , day input from console


# Approach 1: Finding day number using calendar module
import calendar


# User-defined function to get the day of the week from the input date
def get_day_from_date(day_date, day_month, day_year):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]
    # weekday function being used to determine the day of the week on the basis of
    # date, month, year provided
    day_number = calendar.weekday(day_year, day_month, day_date)
    return days[day_number]


# Using try-except block to check whether the date entered is in proper format or not
try:
    date_val = input("Enter date in DD-MM-YYYY format: ")
    # Splitting the date value using split function and storing it in "date", "month",
    # "year" variables
    date, month, year = map(int, date_val.split("-"))
    result = get_day_from_date(date, month, year)
    print(f'Day on {date_val} was {result}')
except ValueError:
    print("Date not in proper format!")
