import math

class Monke:
    threat_reduction = 1
    modulus = 0

    def __init__(self, index: int, items: [], op: str, value: str, worry_value: int, throw_to_when_worry: int,
                 throw_to_when_relaxed: int):
        self.value = 0
        self.special_case = False
        try:
            self.value = int(value)
        except ValueError:
            self.special_case = True

        self.index = index
        self.items = items
        self.op = op
        self.worry_value = worry_value
        self.throw_to_when_worry = throw_to_when_worry
        self.throw_to_when_relaxed = throw_to_when_relaxed
        self.inspect_count = 0

    def handle_worry_multiplications(self):
        self.inspect_count += len(self.items)
        if self.special_case:
            self.items = [((item * item) // self.threat_reduction) for item in self.items]
        elif self.op == '*':
            self.items = [((item * self.value) // self.threat_reduction) for item in self.items]
        elif self.op == '+':
            self.items = [((item + self.value) // self.threat_reduction) for item in self.items]

    def test_and_throw(self, all_monkes: []):
        while len(self.items) > 0:
            item = self.items.pop()
            throw_test = item % self.worry_value == 0
            if throw_test:
                all_monkes[self.throw_to_when_worry].items.append(item % self.modulus)
            else:
                all_monkes[self.throw_to_when_relaxed].items.append(item % self.modulus)
        return all_monkes


def build_monke(index: int, information: str):
    split_info = information.split('\n')
    items = [int(item) for item in split_info[1].lstrip(' Starting items: ').split(', ')]
    op_value = split_info[2].lstrip('Operation: new = old ').split(' ')
    worry_val = split_info[3].lstrip('Test: divisible by ')
    true_val = split_info[4].lstrip('If true: throw to monkey ')
    false_val = split_info[5].lstrip('If false: throw to monkey')
    return Monke(index, items, op_value[0], op_value[1], int(worry_val), int(true_val), int(false_val))


with open('day11.data', 'r') as file:
    data = file.read()
    data_lines = data.split('\n\n')
    monkes = [build_monke(idx, monke_data) for idx, monke_data in enumerate(data_lines)]
    monke_values = [monke.worry_value for monke in monkes if monke.worry_value]
    modulo = math.lcm(*monke_values)
    for monke in monkes:
        monke.modulus = modulo
    for round in range(10_000):
        for monke in monkes:
            monke.handle_worry_multiplications()
            monke.test_and_throw(monkes)

    inspect_count = [monke.inspect_count for monke in monkes]
    inspect_count.sort()
    top2 = inspect_count[::-1][0:2:]
    print(top2[0] * top2[1])
