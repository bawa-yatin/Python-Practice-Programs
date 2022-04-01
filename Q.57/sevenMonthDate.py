# Approach: Using dateutil module

import datetime
from dateutil.relativedelta import relativedelta

input_date = input("Enter date in YYYY-MM-DD format: ")
date_form = datetime.datetime.strptime(input_date, "%Y-%m-%d").date()
six_months = date_form + relativedelta(months=+6)
print(six_months)