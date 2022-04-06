
# Given the month and year as numbers, return whether that month contains
# a Friday 13th.

import datetime
import calendar


# User-defined function to return the response whether the provided month and year
# contains a Friday 13th
def find_month_friday(month, year):
    date1 = f"13 {month} {year}"  # variable holding the date provided by user

    # Variable holding the day of the week in numeric form
    date_obj = datetime.datetime.strptime(date1, '%d %m %Y').weekday()

    # Condition to check if the day of the week is Friday
    if calendar.day_name[date_obj] == 'Friday':
        return "Yes this month has Friday 13th!"
    else:
        return "No this month doesn't have Friday 13th!"


# Using try-except block to verify whether the value of "month" and "year" provided
# are in correct form or not
try:
    month = int(input("Enter a month: "))
    year = int(input("Enter a year: "))
    res = find_month_friday(month, year)
    print(res)  # Variable holding the response returned from the function
except ValueError:
    print("Invalid Value!")
