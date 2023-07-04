class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"[{self.x},{self.y}]"


class SnekPart:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.history = [Point(0, 0)]

    def relocate(self, x: int, y: int):
        self.x = x
        self.y = y
        self.history.append(Point(x, y))


class Snek:
    def __init__(self):
        self.parts = [SnekPart() for _ in range(10)]

    def move(self, motion: str):
        h_prev_x = self.parts.__getitem__(0).x
        h_prev_y = self.parts.__getitem__(0).y
        if motion == 'L':
            self.parts.__getitem__(0).relocate(self.parts.__getitem__(0).x - 1, self.parts.__getitem__(0).y)
        elif motion == 'R':
            self.parts.__getitem__(0).relocate(self.parts.__getitem__(0).x + 1, self.parts.__getitem__(0).y)
        elif motion == 'U':
            self.parts.__getitem__(0).relocate(self.parts.__getitem__(0).x, self.parts.__getitem__(0).y + 1)
        elif motion == 'D':
            self.parts.__getitem__(0).relocate(self.parts.__getitem__(0).x, self.parts.__getitem__(0).y - 1)

        for idx in range(len(self.parts)):
            if idx == len(self.parts) - 1:
                return
            next_part = self.parts.__getitem__(idx + 1)
            ahead_part = self.parts.__getitem__(idx)
            delta_x = abs(next_part.x - ahead_part.x)
            delta_y = abs(next_part.y - ahead_part.y)
            if delta_y == 2 or delta_x == 2:
                p_prev_x = next_part.x
                p_prev_y = next_part.y
                next_part.relocate(h_prev_x, h_prev_y)
                h_prev_x = p_prev_x
                h_prev_y = p_prev_y


with open('day9.data', 'r') as file:
    data = file.read()
    data_lines = data.split('\n')
    instructions = ''.join([el.split(' ')[0] * int(el.split(' ')[1]) for el in data_lines])
    snek = Snek()
    for movement in instructions:
        snek.move(movement)
    print(len(set(snek.parts.__getitem__(len(snek.parts) - 1).history)))
    # solves to 6367
