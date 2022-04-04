# Python program to convert hours and minutes into seconds

# Approach 1

try:
    hours = int(input("Enter number of hours: "))
    minutes = int(input("Enter number of minutes: "))

    if hours >= 1 and minutes >= 1:
        hour_seconds = hours * 3600
        min_seconds = minutes * 60
        total_seconds = hour_seconds + min_seconds
        print("Total seconds in", hours, "hours and", minutes, "minutes is", total_seconds)
    else:
        print("Invalid Value")
except ValueError:
    print("Provide numeric value only!")


# Approach 2: Using Functions

def convertHoursMinToSeconds(hour, minute):
    print("\nUsing Function for converting hours and minutes to seconds")
    hour_second = hour * 3600
    min_second = minute * 60
    print(f"Total seconds are {hour_second + min_second}")


convertHoursMinToSeconds(3, 20)


# Approach 3: Using Classes and Objects

class calcTimeInSeconds:
    def __init__(self, hrs, min):
        self.hrs = hrs
        self.min = min

    def getSeconds(self):
        print("\nUsing Class and Objects for converting hours and minutes to seconds")
        print(f'Total Seconds are {(self.hrs * 3600) + (self.min * 60)}')


c1 = calcTimeInSeconds(3, 15)
c1.getSeconds()
