# Python program to convert hours into seconds
from datetime import timedelta

# Approach 1
try:
    hours = int(input("Enter number of hours: "))
    if hours >= 1:
        seconds = hours * 60 * 60
        print(hours, "hrs have", seconds, "seconds")
    else:
        print("Invalid Value!")
except ValueError:
    print("Provide numeric value only!")


# Approach 2: Using Functions

def convert_hours_to_seconds(hour):
    print("\nUsing Function for converting hours to seconds")
    second = hour * 60 * 60
    print("Seconds:", second)


convert_hours_to_seconds(3)


# Approach 3: Using Classes and Objects

class calcTimeInSeconds:
    def __init__(self, hour):
        self.hour = hour

    def get_seconds(self):
        print(f'\nSeconds in {self.hour} hours are {self.hour * 60 * 60}')


c1 = calcTimeInSeconds(4)
c1.get_seconds()

# Approach 4: Using datetime module
hours = timedelta(hours=5)
secs = hours.total_seconds()
print("Total seconds are", secs)
