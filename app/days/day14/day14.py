from dataclasses import dataclass
from copy import deepcopy


@dataclass
class Point:
    x: int
    y: int
    value: str  # air or wall


def read_file():
    walls = []
    with open("app/days/day14/input.txt", "r") as file:
        for line in file:
            positions = line.strip().split(" -> ")
            coordinates = []
            for position in positions:
                new_coordinates = [int(_) for _ in position.split(",")]
                coordinates.append(new_coordinates)
                walls.append(new_coordinates)
            for index, coordinate in enumerate(coordinates):
                if index < len(coordinates) - 1:
                    x = coordinate[0]
                    y = coordinate[1]
                    x_plus_1 = coordinates[index + 1][0]
                    y_plus_1 = coordinates[index + 1][1]
                    if x == x_plus_1:

                        walls.extend([[x, _] for _ in range(y, y_plus_1 + 1)])
                    elif y == y_plus_1:
                        walls.extend([[_, y] for _ in range(x_plus_1, x + 1)])
    unique_walls = set(tuple(wall) for wall in walls)
    return list(unique_walls)


def get_next_move(x, y, walls: list[tuple], min_x, min_y, max_x, max_y):
    move_one_under = (x, y + 1)
    move_diagonal_left = (x - 1, y + 1)
    move_diagonal_right = (x + 1, y + 1)
    if move_one_under not in walls:
        return move_one_under
    elif move_diagonal_left not in walls:
        return move_diagonal_left
    elif move_diagonal_right not in walls:
        return move_diagonal_right


def first_part():
    walls = read_file()
    print((503,13) in walls)
    old_walls = 0
    min_x = min([wall[0] for wall in walls])
    max_x = max([wall[0] for wall in walls])
    min_y = 0
    max_y = max([wall[1] for wall in walls])
    count = 0
    while old_walls != walls:
        old_walls = deepcopy(walls)
        x_sand = 500
        y_sand = 0
        while True:
            next_move = get_next_move(x_sand, y_sand, walls,
                                      min_x, min_y,
                                      max_x, max_y)
            if next_move:
                (x_sand, y_sand) = next_move
                for line in range(max_y + 1):
                    text = ""
                    for char in range(min_x, max_x + 1):
                        if (char,line) in walls:
                            text += "#"
                        elif (char,line) == (x_sand, y_sand):
                            text +="o"
                        else:
                            text += "."
                    print(line, text)
                print("-"*10)

                if x_sand < min_x or x_sand > max_x or y_sand > max_y:
                    break
                continue
            walls.append((x_sand, y_sand))
            count += 1
            break
    return count



def second_part():
    pass
