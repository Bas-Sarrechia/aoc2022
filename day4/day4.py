class MinMax:
    def __init__(self, range_str: str):
        split = range_str.split('-')
        self.min_val = int(split[0])
        self.max_val = int(split[1])

    def has_overlap(self, other):
        if self.min_val <= other.min_val:
            return self.max_val >= other.min_val
        if other.min_val <= self.min_val:
            return other.max_val >= self.min_val
        return self.min_val == other.min_val or self.max_val == other.max_val

    def contains_range(self, other):
        if self.min_val < other.min_val:
            return self.max_val >= other.max_val
        if other.max_val > self.max_val:
            return other.min_val <= self.min_val
        return self.min_val == other.min_val or self.max_val == other.max_val


def split_and_eval(couple: str):
    split_couple = couple.split(',')
    return MinMax(split_couple[0]).contains_range(MinMax(split_couple[1]))


def split_and_eval_pt2(couple: str):
    split_couple = couple.split(',')
    return MinMax(split_couple[0]).has_overlap(MinMax(split_couple[1]))


with open('day4.data', 'r') as file:
    data = file.read()
    ranges = data.split('\n')

    evaluated_ranges = [split_and_eval(couple) for couple in ranges]
    overlap_ranges = [split_and_eval_pt2(couple) for couple in ranges]

    print(sum(evaluated_ranges))
    print(sum(overlap_ranges))
