
def first_part():
    scenarios = {"AX": 3, "AY": 6, "AZ": 0,
                 "BX": 0, "BY": 3, "BZ": 6,
                 "CX": 6, "CY": 0, "CZ": 3}
    me_points = {"X": 1, "Y": 2, "Z": 3}
    tot = 0
    with open("app/days/day2/input.txt", "r") as file:
        for line in file:
            [opponent, me] = line.strip().split(" ")
            tot += me_points.get(me)
            tot += scenarios.get("".join((opponent, me)))
    return tot


def second_part():
    scenarios = {"AX": 3, "AY": 4, "AZ": 8,
                 "BX": 1, "BY": 5, "BZ": 9,
                 "CX": 2, "CY": 6, "CZ": 7}
    tot = 0
    with open("app/days/day2/input.txt", "r") as file:
        for line in file:
            [opponent, me] = line.strip().split(" ")
            tot += scenarios.get("".join((opponent, me)))
    return tot
