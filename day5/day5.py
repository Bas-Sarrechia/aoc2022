import re


def parse_instruction(instruction_to_parse: str):
    return re.findall('\\d+', instruction_to_parse)


with open('day5.data', 'r') as file:
    data = file.read()
    ranges = data.split('\n')
    stacks = [['P', 'F', 'M', 'Q', 'W', 'G', 'R', 'T'],
              ['H', 'F', 'R'],
              ['P', 'Z', 'R', 'V', 'G', 'H', 'S', 'D'],
              ['Q', 'H', 'P', 'B', 'F', 'W', 'G'],
              ['P', 'S', 'M', 'J', 'H'],
              ['M', 'Z', 'T', 'H', 'S', 'R', 'P', 'L'],
              ['P', 'T', 'H', 'N', 'M', 'L'],
              ['F', 'D', 'Q', 'R'],
              ['D', 'S', 'C', 'N', 'L', 'P', 'H']]

    for instruction in ranges:
        parsed = [int(i) for i in parse_instruction(instruction)]
        pt1 = -1
        pt2 = 1
        fromStack = parsed[1] - 1
        toStack = parsed[2] - 1
        amount = parsed[0]
        source = stacks[fromStack]
        move = source[-amount:]
        modified_source = source[:-amount]
        modified_target = stacks.__getitem__(toStack)
        modified_target.extend(move[::pt2])
        stacks[fromStack] = modified_source
        stacks[toStack] = modified_target
    print(''.join([stack_top.pop() for stack_top in stacks]))
