def first_part():
    tot = 0
    calories = []
    with open("app/days/day1/input.txt", "r") as file:
        for line in file:
            row = line.strip()
            if row.isnumeric():
                tot += int(row)
            else:
                calories.append(tot)
                tot = 0
    calories.sort()
    return calories[-1]


def second_part():
    tot = 0
    calories = []
    with open("app/days/day1/input.txt", "r") as file:
        for line in file:
            row = line.strip()
            if row.isnumeric():
                tot += int(row)
            else:
                calories.append(tot)
                tot = 0
    calories.sort()
    return sum(calories[-3::])