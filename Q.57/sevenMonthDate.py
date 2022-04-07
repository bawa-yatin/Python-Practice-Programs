
# Calculate the date 7 month from any date, take date input from console

# Approach: Using Datetime and Dateutil's relativedelta module

import datetime
from dateutil.relativedelta import relativedelta

# Using try-except block to check whether the date entered is in proper format or not
try:
    input_date = input("Enter date in YYYY-MM-DD format: ")
    date_form = datetime.datetime.strptime(input_date, "%Y-%m-%d").date()
    six_months = date_form + relativedelta(months=+6)
    print(six_months)
except ValueError:
    print("Date not in proper format!")