import json


def get_pairs():
    pairs = []
    with open("app/days/day13/input.txt", "r") as file:
        for index, line in enumerate(file):
            pair = index // 3
            if index % 3 == 0:
                pairs.append([json.loads(line.strip())])
            elif index % 3 == 1:
                pairs[pair].append(json.loads(line.strip()))
    return pairs


def get_all_packets():
    packets = []
    with open("app/days/day13/input.txt", "r") as file:
        for line in file:
            if line.strip():
                packets.append(json.loads(line.strip()))
    return packets


def compare_pair(first_pair, second_pair):
    for index, element in enumerate(first_pair):
        try:
            second_element = second_pair[index]
        except:
            return -1
        if type(element) == int and type(second_element) == int:
            if element < second_pair[index]:
                return 1
            elif element > second_pair[index]:
                return -1
        elif type(element) == list and type(second_element) == int:
            new_compare = compare_pair(element, [second_element])
            if new_compare != 0:
                return new_compare
        elif type(element) == int and type(second_element) == list:
            new_compare = compare_pair([element], second_element)
            if new_compare != 0:
                return new_compare
        elif type(element) == list and type(second_element) == list:
            new_compare = compare_pair(element, second_element)
            if new_compare != 0:
                return new_compare
    if len(second_pair) > len(first_pair):
        return 1
    return 0


def first_part():
    pairs = get_pairs()
    tot = 0
    for index, pair in enumerate(pairs):
        first_pair = pair[0]
        second_pair = pair[1]
        if compare_pair(first_pair, second_pair) == 1:
            tot += index + 1
    return tot


def second_part():
    packets = get_all_packets()
    packets.append([[2]])
    packets.append([[6]])
    tot = 1
    for packet in packets:
        if packet == [[2]] or packet == [[6]]:
            tot *= abs(sum(
                [_ for _ in list(map(lambda p: compare_pair(packet, p),
                                     packets)) if _ < 0])) + 1
    return tot




