import re
from typing import Optional


class Directory:
    def __init__(self, name):
        self.name = name
        self.children: list[Directory] = []
        self.size = 0
        self.parent: Optional[Directory] = None


tot = 0
sizes = []


def first_part():
    initial_directory = Directory("root")
    current_directory = initial_directory
    with open("app/days/day7/input.txt", "r") as file:
        for line in file:
            line = line.strip()
            new_directory = re.findall(r"\$ cd (.*)", line)[0] if re.findall(r"\$ cd (.*)", line) else None
            listed_directory = re.findall(r"dir (.*)", line)[0] if re.findall(r"dir (.*)", line) else None
            file = re.findall(r"([0-9]*)", line)[0] if re.findall(r"([0-9]*)", line)[0] else None
            if new_directory:
                if new_directory.count("..") > 0:
                    for _ in range(new_directory.count("..")):
                        current_directory = current_directory.parent
                else:
                    for child in current_directory.children:
                        if child.name == new_directory:
                            current_directory = child
            if listed_directory:
                added_directory = Directory(listed_directory)
                added_directory.parent = current_directory
                current_directory.children.append(added_directory)
            if file:
                current_directory.size += int(file)

    def calculate_size(directory: Directory):
        global tot
        if len(directory.children) == 0:
            size = directory.size
            if size <= 100000:
                tot += size
            return size
        else:
            directory.size += sum(
                calculate_size(child) for child in directory.children)
            size = directory.size
            if size <= 100000:
                tot += size
            sizes.append(size)
            return size

    calculate_size(initial_directory)
    return tot


def second_part():
    initial_directory = Directory("root")
    current_directory = initial_directory
    with open("app/days/day7/input.txt", "r") as file:
        for line in file:
            line = line.strip()
            new_directory = re.findall(r"\$ cd (.*)", line)[0] if re.findall(
                r"\$ cd (.*)", line) else None
            listed_directory = re.findall(r"dir (.*)", line)[0] if re.findall(
                r"dir (.*)", line) else None
            file = re.findall(r"([0-9]*)", line)[0] if \
            re.findall(r"([0-9]*)", line)[0] else None
            if new_directory:
                if new_directory.count("..") > 0:
                    for _ in range(new_directory.count("..")):
                        current_directory = current_directory.parent
                else:
                    for child in current_directory.children:
                        if child.name == new_directory:
                            current_directory = child
            if listed_directory:
                added_directory = Directory(listed_directory)
                added_directory.parent = current_directory
                current_directory.children.append(added_directory)
            if file:
                current_directory.size += int(file)

    def calculate_size(directory: Directory):
        global sizes
        if len(directory.children) == 0:
            size = directory.size
            sizes.append(size)
            return size
        else:
            directory.size += sum(
                calculate_size(child) for child in directory.children)
            size = directory.size
            sizes.append(size)
            return size

    calculate_size(initial_directory)
    sizes.sort()
    available_space = 70000000 - sizes[-1]
    for size in sizes:
        if available_space + size > 30000000:
            break
    return size
