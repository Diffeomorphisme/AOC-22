def move(head: dict, tail: dict):
    distance = calculate_distance(head, tail)
    if distance[2] > 2:
        tail['row'] += int(distance[0] / abs(distance[0]))
        tail['column'] += int(distance[1] / abs(distance[1]))
    elif distance[2] == 2:
        if abs(distance[0]) > 1:
            tail['row'] += int(distance[0]/abs(distance[0]))
        else:
            tail['column'] += int(distance[1] / abs(distance[1]))
    return tail


def calculate_distance(head: dict, tail: dict):
    return (head.get('row') - tail.get('row'),
            head.get('column') - tail.get('column'),
            ((head.get('row') - tail.get('row'))**2
             + (head.get('column') - tail.get('column'))**2)**0.5)


def move_head(direction: str, head: dict):
    if direction == "R":
        head['column'] += 1
    elif direction == "L":
        head['column'] -= 1
    elif direction == "U":
        head['row'] -= 1
    elif direction == "D":
        head['row'] += 1
    return head


def first_part():
    head = {"row": 0, "column": 0}
    tail = head.copy()
    visited = set()
    with open("app/days/day9/input.txt", "r") as file:
        for line in file:
            direction, iteration = line.strip().split()
            for _ in range(int(iteration)):
                head = move_head(direction, head)
                tail = move(head, tail)
                visited.add((tail.get('row'), tail.get('column')))
    return len(visited)


def second_part():
    head = {"row": 0, "column": 0}
    body = [head.copy() for _ in range(10)]
    visited = set()
    with open("app/days/day9/input.txt", "r") as file:
        for line in file:
            direction, iteration = line.strip().split()
            for _ in range(int(iteration)):
                body[0] = move_head(direction, body[0])
                for index, element in enumerate(body):
                    if index < len(body) - 1:
                        body[index + 1] = move(body[index], body[index+1])
                visited.add((body[-1].get('row'), body[-1].get('column')))
    return len(visited)
