def pointsCalculate(win, loss, draw):
    won = win * 3
    lose = loss * 0
    drawn = draw * 1
    totalScore = won + lose + drawn
    return totalScore


team_1 = pointsCalculate(7, 4, 1)
team_2 = pointsCalculate(6, 3, 3)

print("Points scored by Team 1 are", team_1)
print("Points scored by Team 2 are", team_2)