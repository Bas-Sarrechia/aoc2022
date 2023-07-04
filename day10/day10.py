with open('day10.data', 'r') as file:
    data = file.read()
    data_lines = data.split('\n')

    cycle = 0
    signal_strength = 1
    search_cycles = [20, 60, 100, 140, 180, 220]
    found_signal_strengths = []
    increment_value = 0
    for instruction in data_lines:
        if search_cycles.__contains__(cycle):
            found_signal_strengths.append(signal_strength)
        signal_strength += increment_value
        if instruction == 'noop':
            cycle += 1
            increment_value = 0
        else:
            [_, value] = instruction.split(' ')
            cycle += 1
            if search_cycles.__contains__(cycle):
                found_signal_strengths.append(signal_strength)
            cycle += 1
            increment_value = int(value)
    print(sum([modifier * strength for (strength, modifier) in zip(found_signal_strengths, search_cycles)]))
