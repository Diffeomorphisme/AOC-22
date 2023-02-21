def first_part():
    cycle_checks = [20, 60, 100, 140, 180, 220]
    signal_strength = []
    register = 1
    cycle = 1
    with open("app/days/day10/input.txt", "r") as file:
        for line in file:
            line = line.strip().split()
            if len(line) == 1:
                signal_strength, cycle = tick(cycle, cycle_checks,
                                              register, signal_strength)
            else:
                for _ in range(2):
                    signal_strength, cycle = tick(cycle, cycle_checks,
                                                  register, signal_strength)
                register += int(line[1])
    return sum(signal_strength)


def tick(cycle, cycle_checks, register, signal_strength):
    if cycle in cycle_checks:
        signal_strength.append(register * cycle)
    cycle += 1
    return signal_strength, cycle


def tick_2(cycle: int, pixel_lines: list[list],
           current_line: list, register: int):
    if cycle % 40 == 1:
        pixel_lines.append([])
        current_line = pixel_lines[-1]
    index = cycle % 40 - 1
    (current_line.append("#") if register - 1 <= index <= register + 1
     else current_line.append("."))
    cycle += 1
    return current_line, pixel_lines, cycle


def second_part():
    pixel_lines = []
    current_line = []
    register = 1
    cycle = 1
    with open("app/days/day10/input.txt", "r") as file:
        for line in file:
            line = line.strip().split()
            if len(line) == 1:
                current_line, pixel_lines, cycle = tick_2(
                    cycle, pixel_lines, current_line, register)
            else:
                for _ in range(2):
                    current_line, pixel_lines, cycle = tick_2(
                        cycle, pixel_lines, current_line, register)
                register += int(line[1])
    return "\n".join(["".join([char for char in line]) for line in pixel_lines])
