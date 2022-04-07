# Python program to trace the movement of the robot

from math import sqrt


# User-defined function to return the total distance from the current position
# after a sequence of movement and original point.
def robot_movement(moves):
    pos = [0, 0]  # Variable holding the initial position of the robot
    for move in moves:
        dir_and_distance = move.split()
        if dir_and_distance[0].upper() == "UP":
            pos[0] += int(dir_and_distance[1])
        elif dir_and_distance[0].upper() == "DOWN":
            pos[0] -= int(dir_and_distance[1])
        elif dir_and_distance[0].upper() == "RIGHT":
            pos[1] += int(dir_and_distance[1])
        elif dir_and_distance[0].upper() == "LEFT":
            pos[1] -= int(dir_and_distance[1])

    return round(sqrt(pos[0] ** 2 + pos[1] ** 2))


moves_list = []  # List Variable holding the movement of robot in different directions
for i in range(4):
    step_dir_and_dist = input("Type in UP/DOWN/LEFT/RIGHT along with step number: ")
    moves_list.append(step_dir_and_dist)

distance = robot_movement(moves_list)  # Variable holding the response returned
# from the "robot_movement" function
print(distance)
