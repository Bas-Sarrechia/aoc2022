def split_string_in_equal_halves(code: str):
    length = int(len(code) / 2)
    return [code[:length], code[length:]]


def find_unique(a: str, b: str):
    for i in [*a]:
        if b.find(i) != -1:
            return i
    return ''


def find_common(args: str):
    found_elements = {}
    for i in args:
        pushed_letters = []
        for k in [*i]:
            if not pushed_letters.__contains__(k):
                found_elements[k] = found_elements.get(k, 0) + 1
                pushed_letters.append(k)
            if found_elements[k] == 3:
                return k


def score(ch):
    return ord(ch) - 96 if ch[0].islower() else ord(ch) - 38


with open('day3.data', 'r') as file:
    data = file.read()
    codes = data.split('\n')
    split_codes = list(map(split_string_in_equal_halves, codes))
    unique_codes = list(map(lambda code: find_unique(code[0], code[1]), split_codes))
    scored = list(
        map(score, unique_codes)
    )

    grouped_codes = nested_list = [codes[i:i + 3] for i in range(0, len(codes), 3)]
    common_codes = list(map(find_common, grouped_codes))

    scored_p2 = list(
        map(score, common_codes)
    )
    print(sum(scored), sum(scored_p2))
