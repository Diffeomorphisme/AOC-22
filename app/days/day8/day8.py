def first_part():
    numbers = []
    with open("app/days/day8/input.txt", "r") as file:
        for line in file:
            numbers.append([int(char) for char in line.strip()])

    tot = 0
    for line_index, line in enumerate(numbers):
        # First/last line
        if line_index == 0 or line_index == len(numbers) - 1:
            tot += len(line)
        else:
            for column_index, tree in enumerate(line):
                # First/last tree
                if column_index == 0 or column_index == len(line) - 1:
                    tot += 1
                else:
                    if (tree > max(line[:column_index]) or
                            tree > max(line[column_index + 1:]) or
                            tree > max([numbers[i][column_index]
                                        for i in range(line_index)]) or
                            tree > max([numbers[i][column_index]
                                        for i in
                                        range(line_index + 1, len(numbers))])
                    ):
                        tot += 1
    return tot


def second_part():

    def look_any_direction(value, trees):
        for index, tree in enumerate(trees):
            if tree >= value:
                return index + 1
        return len(trees)

    numbers = []
    with open("app/days/day8/input.txt", "r") as file:
        for line in file:
            numbers.append([int(char) for char in line.strip()])

    maximum = 0
    for line_index, line in enumerate(numbers):
        for column_index, tree in enumerate(line):
            score = 1
            # look right
            if column_index < len(line) - 1:
                score *= look_any_direction(tree, line[column_index + 1:])
            else:
                continue
            # look left
            if column_index > 0:
                input = line[:column_index]
                input = input[::-1]
                score *= look_any_direction(tree, input)
            else:
                continue
            # look down
            if line_index < len(numbers) - 1:
                input = [numbers[i][column_index] for i in
                         range(line_index + 1, len(numbers))]
                score *= look_any_direction(tree, input)
            else:
                continue
            # look up
            if line_index > 0:
                input = [numbers[i][column_index]
                     for i in range(line_index)]
                input = input[::-1]
                score *= look_any_direction(tree, input)
            else:
                continue
            if score > maximum:
                maximum = score
    return maximum
