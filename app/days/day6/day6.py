class Packet:
    def __init__(self, size_packet):
        self.group = ["" for i in range(size_packet)]

    def add_character(self, char):
        self.group.append(char)
        self.group.pop(0)

    def check_start_packet(self):
        for char in self.group:
            if self.group.count(char) > 1:
                return False
        return True


def first_part():
    with open("app/days/day6/input.txt") as file:
        packet = Packet(4)
        for line in file:
            for index, char in enumerate(line.strip()):
                packet.add_character(char)
                if index > 2:
                    if packet.check_start_packet():
                        return index + 1


def second_part():
    with open("app/days/day6/input.txt") as file:
        packet = Packet(14)
        for line in file:
            for index, char in enumerate(line.strip()):
                packet.add_character(char)
                if index > 2:
                    if packet.check_start_packet():
                        return index + 1