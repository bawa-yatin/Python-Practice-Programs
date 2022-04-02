from math import sqrt


def robot_movement(moves):
    pos = [0, 0]
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


moves_list = []
for i in range(4):
    step_dir_and_dist = input("Type in UP/DOWN/LEFT/RIGHT along with step number: ")
    moves_list.append(step_dir_and_dist)

distance = robot_movement(moves_list)
print(distance)