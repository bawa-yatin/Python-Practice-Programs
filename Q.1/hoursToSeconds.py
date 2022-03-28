# Python program to convert hours into seconds
from datetime import timedelta

# Approach 1

hours = int(input("Enter number of hours: "))
seconds = hours * 60 * 60
print(hours, "hrs have", seconds, "seconds")


# Approach 2: Using Functions

def convertHoursToSeconds(hour):
    print("\nUsing Function for converting hours to seconds")
    second = hour * 60 * 60
    print("Seconds:", second)


convertHoursToSeconds(3)


# Approach 3: Using Classes and Objects

class calcTimeInSeconds:
    def __init__(self, hour):
        self.hour = hour

    def getSeconds(self):
        print(f'\nSeconds in {self.hour} hours are {self.hour * 60 * 60}')


c1 = calcTimeInSeconds(4)
c1.getSeconds()

# Approach 4: Using datetime module
hours = timedelta(hours=5)
secs = hours.total_seconds()
print("Total seconds are", secs)
