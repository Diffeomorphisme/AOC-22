
char_map = []
alphabet = "abcdefghijklmnopqrstuvwxEyzS"
with open("app/days/day12/input.txt", "r") as file:
    for line in file:
        char_map.append([char for char in line.strip()])

start: dict
end: dict

nr_rows = len(char_map)
nr_columns = 0

for index, row in enumerate(char_map):
    char_map[index] = list(map(lambda x: alphabet.index(x), row))
    if "S" in row:
        place = row.index("S")
        start = {"coordinates": [index, place], "value": 0}
        char_map[index][place] = 0
    if "E" in row:
        end = {"coordinates": [index, row.index("E")],
               "value": alphabet.index("E")}
    nr_columns = len(row)


def move_up(coordinates: list[int]):
    return [coordinates[0] - 1, coordinates[1]]


def move_down(coordinates: list[int]):
    return [coordinates[0] + 1, coordinates[1]]


def move_right(coordinates: list[int]):
    return [coordinates[0], coordinates[1] + 1]


def move_left(coordinates: list[int]):
    return [coordinates[0], coordinates[1] - 1]


def can_move_up(coordinates: list[int], visited):
    if coordinates[0] > 0:
        if (
                char_map[coordinates[0] - 1][coordinates[1]] -
                char_map[coordinates[0]][coordinates[1]]
                <= 1 and not visited[coordinates[0] - 1][coordinates[1]]):
            return True
    return False


def can_move_down(coordinates: list[int], visited):
    if coordinates[0] < nr_rows - 1:
        if (
                char_map[coordinates[0] + 1][coordinates[1]] -
                char_map[coordinates[0]][coordinates[1]]
                <= 1 and not visited[coordinates[0] + 1][coordinates[1]]):
            return True
    return False


def can_move_left(coordinates: list[int], visited):
    if coordinates[1] > 0:
        if (
                char_map[coordinates[0]][coordinates[1] - 1] -
                char_map[coordinates[0]][coordinates[1]]
                <= 1 and not visited[coordinates[0]][coordinates[1] - 1]):
            return True
    return False


def can_move_right(coordinates: list[int], visited):
    if coordinates[1] < nr_columns - 1:
        if (
                char_map[coordinates[0]][coordinates[1] + 1] -
                char_map[coordinates[0]][coordinates[1]]
                <= 1 and not visited[coordinates[0]][coordinates[1] + 1]):
            return True
    return False


def find_possible_moves(coordinates: list[int], visited: list):
    movements = []
    if can_move_up(coordinates, visited):
        movements.append(move_up(coordinates))
    if can_move_down(coordinates, visited):
        movements.append(move_down(coordinates))
    if can_move_left(coordinates, visited):
        movements.append(move_left(coordinates))
    if can_move_right(coordinates, visited):
        movements.append(move_right(coordinates))
    return movements


def calculate_distance_to_goal(front: list, visited: list[list[bool]]):
    generations = 0
    while True:
        for coordinates in front:
            visited[coordinates[0]][coordinates[1]] = True

        if end.get("coordinates") in front:
            return generations + 1
        possible_moves = []
        for element in front:
            possible_moves.extend([move for move in
                                   find_possible_moves(element, visited)])
        if not possible_moves:
            return generations + 1000
        front = [list(item) for item in set(tuple(move)
                                            for move in possible_moves)]
        generations += 1


def first_part():
    # Somehow I am falling 3 short...
    visited = [[False for _ in range(nr_columns)] for _ in range(nr_rows)]
    return calculate_distance_to_goal([start.get("coordinates")],
                                      visited) + 3


def second_part():
    distances = []
    for row_index, row in enumerate(char_map):
        for column_index, column in enumerate(row):

            if char_map[row_index][column_index] == 0:
                visited = [[False for _ in range(nr_columns)]
                           for _ in range(nr_rows)]
                distances.append(calculate_distance_to_goal(
                    [[row_index, column_index]], visited) + 3)
    return min(distances)
