import datetime
import calendar


def findMonthFriday(month, year):
    date1 = f"13 {month} {year}"
    date_obj = datetime.datetime.strptime(date1, '%d %m %Y').weekday()
    if calendar.day_name[date_obj] == 'Friday':
        return "Yes this month has Friday 13th!"
    else:
        return "No this month doesn't have Friday 13th!"


try:
    month = int(input("Enter a month: "))
    year = int(input("Enter a year: "))
    res = findMonthFriday(month, year)
    print(res)
except ValueError:
    print("Invalid Value!")
