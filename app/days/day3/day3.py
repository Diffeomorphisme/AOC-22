items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def first_part():
    tot = 0
    with open("app/days/day3/input.txt", "r") as file:
        for line in file:
            stripped_line = line.strip()
            line1, line2 = (stripped_line[:len(stripped_line)//2],
                            stripped_line[len(stripped_line)//2:])
            for char in line1:
                if char in line2:
                    tot += items.index(char) + 1
                    break
    return tot


def second_part():
    class Queue:
        def __init__(self):
            self.group = ["", "", ""]

        def add_elf(self, new_elf: str):
            self.group.append(new_elf)
            self.group.pop(0)

        def find_badge(self):

            for char in self.group[0]:
                if char in group.group[1] and char in group.group[2]:
                    return char

    tot = 0
    index = 1
    group = Queue()
    with open("app/days/day3/input.txt", "r") as file:
        for line in file:
            stripped_line = line.strip()
            group.add_elf(stripped_line)
            if index % 3 == 0:
                badge = group.find_badge()
                if badge:
                    tot += items.index(badge) + 1
            index += 1
    return tot
