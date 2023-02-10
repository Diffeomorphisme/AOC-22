import re


class Stack:
    def __init__(self):
        self.pile = []

    def build_pile(self, box):
        self.pile.insert(-0, box)

    def add_box(self, box):
        self.pile.append(box)

    def remove_box(self):
        return self.pile.pop()

    def add_boxes(self, boxes):
        self.pile += boxes

    def remove_boxes(self, number):
        removed_boxes = self.pile[-number:]
        for _ in range(number):
            self.pile.pop()
        return removed_boxes


def first_part():

    stacks: list[Stack]
    first_line = True
    instructions = False
    with open("app/days/day5/input.txt", "r") as file:
        for line in file:
            if instructions:
                if line.strip():
                    digits = [int(x) for x in re.findall(r"([0-9]+)", line.strip())]
                    for i in range(digits[0]):
                        box_moved = stacks[digits[1] - 1].remove_box()
                        stacks[digits[2] - 1].add_box(box_moved)
            else:
                if any(char.isdigit() for char in line):
                    instructions = True
                    continue
                if first_line:
                    stacks = [Stack() for _ in range(len(line) // 4)]
                    first_line = False
                for index, char in enumerate(line):
                    if index % 4 == 1:
                        if char != " ":
                            stacks[index//4].build_pile(char)
    return "".join([stack.pile[-1] for stack in stacks])


def second_part():
    stacks: list[Stack]
    first_line = True
    instructions = False
    with open("app/days/day5/input.txt", "r") as file:
        for line in file:
            if instructions:
                if line.strip():
                    digits = [int(x) for x in
                              re.findall(r"([0-9]+)", line.strip())]
                    boxes_moved = stacks[digits[1] - 1].remove_boxes(digits[0])
                    stacks[digits[2] - 1].add_boxes(boxes_moved)
            else:
                if any(char.isdigit() for char in line):
                    instructions = True
                    continue
                if first_line:
                    stacks = [Stack() for _ in range(len(line) // 4)]
                    first_line = False
                for index, char in enumerate(line):
                    if index % 4 == 1:
                        if char != " ":
                            stacks[index // 4].build_pile(char)
    return "".join([stack.pile[-1] for stack in stacks])