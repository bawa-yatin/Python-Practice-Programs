# Python program to calculate age to days

from datetime import datetime

# Approach 1:

try:
    user_age = int(input("Enter any age: "))
    if user_age >= 1:
        current_year = datetime.now().year
        birth_year = current_year - user_age

        leap_year_count = 0
        for i in range(1, user_age + 1):
            temp = birth_year
            if (temp % 400 == 0) and (temp % 100 == 0):
                leap_year_count += 1
            elif (temp % 4 == 0) and (temp % 100 != 0):
                leap_year_count += 1

        total_age_days = ((user_age - leap_year_count) * 365) + (leap_year_count * 366)
        print(total_age_days)
    else:
        print("Invalid Age!")
except ValueError:
    print("Provide numeric value only!")


# Approach 2: Using Function

def calculate_age_in_days(age):
    present_year = datetime.now().year
    user_birth_year = present_year - age

    leap_year = 0
    for i in range(1, age + 1):
        temp1 = user_birth_year
        if (temp1 % 400 == 0) and (temp1 % 100 == 0):
            leap_year += 1
        elif (temp1 % 4 == 0) and (temp1 % 100 != 0):
            leap_year += 1

    total_days = ((age - leap_year) * 365) + (leap_year * 366)
    print("\nUsing Function")
    print(total_days)


calculate_age_in_days(33)


# Approach 3: Using Class

class calculateAgeDays:
    def __init__(self, age_user):
        self.age_user = age_user

    def get_age_days(self):
        present_year = datetime.now().year
        user_birth_year = present_year - self.age_user

        leap_year = 0
        for i in range(1, self.age_user + 1):
            temp1 = user_birth_year
            if (temp1 % 400 == 0) and (temp1 % 100 == 0):
                leap_year += 1
            elif (temp1 % 4 == 0) and (temp1 % 100 != 0):
                leap_year += 1

        total_days = ((self.age_user - leap_year) * 365) + (leap_year * 366)
        print("\nUsing Class")
        print(total_days)


cd = calculateAgeDays(18)
cd.get_age_days()
