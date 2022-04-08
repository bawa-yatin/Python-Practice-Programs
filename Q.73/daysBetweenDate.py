
# Create a function that takes two dates and returns the number of days between the
# first and second date.

# Using datetime module to calculate number of days
import datetime


def num_of_days(fdate, sdate):
    return (sdate - fdate).days


try:
    date_1 = input("Enter date in YYYY-MM-DD format: ")
    date_2 = input("Enter date in YYYY-MM-DD format: ")
    # variable containing the first date value
    first_date = datetime.datetime.strptime(date_1, "%Y-%m-%d").date()
    # variable containing the second date value
    second_date = datetime.datetime.strptime(date_2, "%Y-%m-%d").date()
    # variable containing number of days between first date and second date
    days = num_of_days(first_date, second_date)
    print(days, "days")
except ValueError:
    print("Date not in proper format!")
