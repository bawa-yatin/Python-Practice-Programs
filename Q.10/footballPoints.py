# Football Points

# Create a function that takes the number of wins, draws and losses and calculates
# the number of points a football team has obtained so far.

# wins get 3 points
# draws get 1 point
# losses get 0 points

# User-defined function to calculate the total number of points scored by football team
def points_calculate(win, loss, draw):
    won = win * 3  # variable for holding the total points achieved after winning games
    lose = loss * 0  # variable for holding the total points achieved after losing games
    drawn = draw * 1  # variable for holding the total points achieved after games were drawn
    total_score = won + lose + drawn  # variable for holding the total points achieved
    return total_score


team_1 = points_calculate(7, 4, 1)  # Variable holding the response returned from the function
team_2 = points_calculate(6, 3, 3)

print("Points scored by Team 1 are", team_1)
print("Points scored by Team 2 are", team_2)
