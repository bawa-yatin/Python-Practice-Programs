import datetime


def numOfDays(fdate, sdate):
    return (sdate - fdate).days


try:
    date_1 = input("Enter date in YYYY-MM-DD format: ")
    date_2 = input("Enter date in YYYY-MM-DD format: ")
    first_date = datetime.datetime.strptime(date_1, "%Y-%m-%d").date()
    second_date = datetime.datetime.strptime(date_2, "%Y-%m-%d").date()
    days = numOfDays(first_date, second_date)
    print(days, "days")
except ValueError:
    print("Date not in proper format!")
