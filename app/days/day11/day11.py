from math import trunc


class Monkey:
    def __init__(self, items: list[int], test, outcome_true, outcome_false):
        self.items = items
        self.test = test
        self.outcome_true = outcome_true
        self.outcome_false = outcome_false
        self.number_items_inspected = 0

    def operation(self, item):
        pass

    @staticmethod
    def relief(item, tot=None):
        if tot:
            return item % tot
        else:
            return trunc(item/3)

    def send_item_to_other_monkeys(self, item):
        if item % self.test == 0:
            monkeys[self.outcome_true].items.append(item)
        else:
            monkeys[self.outcome_false].items.append(item)

    def do_full_cycle(self, tot=None):
        for item in self.items:
            new_item = self.operation(item)
            self.number_items_inspected += 1
            if tot:
                new_item = self.relief(new_item, tot)
            else:
                new_item = self.relief(new_item)
            self.send_item_to_other_monkeys(new_item)
        self.items = []


# class Monkey0(Monkey):
#     def operation(self, item):
#         return item * 19
#
#
# class Monkey1(Monkey):
#     def operation(self, item):
#         return item + 6
#
#
# class Monkey2(Monkey):
#     def operation(self, item):
#         return item ** 2
#
#
# class Monkey3(Monkey):
#     def operation(self, item):
#         return item + 3

class Monkey0(Monkey):
    def operation(self, item):
        return item * 3


class Monkey1(Monkey):
    def operation(self, item):
        return item * 11


class Monkey2(Monkey):
    def operation(self, item):
        return item + 6


class Monkey3(Monkey):
    def operation(self, item):
        return item + 4


class Monkey4(Monkey):
    def operation(self, item):
        return item + 8


class Monkey5(Monkey):
    def operation(self, item):
        return item + 2


class Monkey6(Monkey):
    def operation(self, item):
        return item ** 2


class Monkey7(Monkey):
    def operation(self, item):
        return item + 5


# monkey0 = Monkey0(items=[79, 98], test=23, outcome_true=2, outcome_false=3)
# monkey1 = Monkey1(items=[54, 65, 75, 74], test=19, outcome_true=2,
#                   outcome_false=0)
# monkey2 = Monkey2(items=[79, 60, 97], test=13, outcome_true=1,
#                   outcome_false=3)
# monkey3 = Monkey3(items=[74], test=17, outcome_true=0,
#                   outcome_false=1)


monkey0 = Monkey0(items=[54, 53], test=2, outcome_true=2, outcome_false=6)
monkey1 = Monkey1(items=[95, 88, 75, 81, 91, 67, 65, 84], test=7, outcome_true=3,
                  outcome_false=4)
monkey2 = Monkey2(items=[76, 81, 50, 93, 96, 81, 83], test=3, outcome_true=5,
                  outcome_false=1)
monkey3 = Monkey3(items=[83, 85, 85, 63], test=11, outcome_true=7,
                  outcome_false=4)
monkey4 = Monkey4(items=[85, 52, 64], test=17, outcome_true=0,
                  outcome_false=7)
monkey5 = Monkey5(items=[57], test=5, outcome_true=1, outcome_false=3)
monkey6 = Monkey6(items=[60, 95, 76, 66, 91], test=13, outcome_true=2,
                  outcome_false=5)
monkey7 = Monkey7(items=[65, 84, 76, 72, 79, 65], test=19, outcome_true=6,
                  outcome_false=0)

monkeys: list[Monkey] = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5,
                         monkey6, monkey7]

# monkeys: list[Monkey] = [monkey0, monkey1, monkey2, monkey3]


def first_part():
    return 1
    for _ in range(20):
        for monkey in monkeys:
            monkey.do_full_cycle()
    sorted_monkeys = sorted(monkeys, key=lambda x: x.number_items_inspected)
    monkey_business = sorted_monkeys[-1].number_items_inspected * sorted_monkeys[-2].number_items_inspected
    return monkey_business


def second_part():
    tot = 1
    for monkey in monkeys:
        tot *= monkey.test
    for _ in range(10000):
        for monkey in monkeys:
            monkey.do_full_cycle(tot=tot)
    print([monkey.number_items_inspected for monkey in monkeys])
    sorted_monkeys = sorted(monkeys, key=lambda x: x.number_items_inspected)
    print([sorted_monkey.number_items_inspected for sorted_monkey in sorted_monkeys])
    monkey_business = sorted_monkeys[-1].number_items_inspected * sorted_monkeys[-2].number_items_inspected
    return monkey_business