from datetime import date


def numOfDays(fdate, sdate):
    return (sdate-fdate).days


date_1 = input("Enter date in YYYY-MM-DD format: ")
date_2 = input("Enter date in YYYY-MM-DD format: ")
date1, month1, year1 = map(int, date_1.split("-"))
date2, month2, year2 = map(int, date_2.split("-"))

first_date = date(year1, month1, date1)
second_date = date(year2, month2, date2)
days = numOfDays(first_date, second_date)
print(days, "days")