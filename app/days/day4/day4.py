def first_part():
    with open("app/days/day4/input.txt", "r") as file:
        tot = 0
        for line in file:
            line = line.strip().split(",")
            [elf1, elf2] = [list(map(int, elf.split("-"))) for elf in line]
            if (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]) or (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]):
               tot += 1
        return tot


def second_part():
    with open("app/days/day4/input.txt", "r") as file:
        tot = 0
        for line in file:
            line = line.strip().split(",")
            [elf1, elf2] = [list(map(int, elf.split("-"))) for elf in line]
            if ((elf2[0] <= elf1[0] <= elf2[1]) or
                    (elf2[0] <= elf1[1] <= elf2[1]) or
                    (elf1[0] <= elf2[0] <= elf1[1]) or
                    (elf1[0] <= elf2[1] <= elf1[1])):
                tot += 1
        return tot
