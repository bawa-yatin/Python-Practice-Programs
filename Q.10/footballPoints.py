def pointsCalculate(win, loss, draw):
    won = win * 3
    lose = loss * 0
    drawn = draw * 1
    total_score = won + lose + drawn
    return total_score


team_1 = pointsCalculate(7, 4, 1)
team_2 = pointsCalculate(6, 3, 3)

print("Points scored by Team 1 are", team_1)
print("Points scored by Team 2 are", team_2)