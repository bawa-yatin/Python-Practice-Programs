# Calculate no of days between two date , take input from console

# Approach One: Using datetime library and using strptime function
import datetime


# User-defined function to calculate no of days between two date
def num_of_days(fdate, sdate):
    return (sdate - fdate).days


# Using try-except block to check whether the date entered is in proper format or not
try:
    date_1 = input("Enter date in YYYY-MM-DD format: ")
    date_2 = input("Enter date in YYYY-MM-DD format: ")
    # Obtaining day, month, year using strptime()
    first_date = datetime.datetime.strptime(date_1, "%Y-%m-%d").date()
    second_date = datetime.datetime.strptime(date_2, "%Y-%m-%d").date()
    days = num_of_days(first_date, second_date)  # Variable holding the response returned from the function
    print(days, "days")
except ValueError:
    print("Date not in proper format!")
