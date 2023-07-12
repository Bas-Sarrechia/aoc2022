def get_lit_pixel(current_pos: int, pixels_pos: int):
    if pixels_pos - 1 <= (current_pos % 40) <= pixels_pos + 1:
        return '#'
    return ' '


with open('day10.data', 'r') as file:
    data = file.read()
    data_lines = data.split('\n')

    cycle = 0
    signal_strength = 1
    search_cycles = [20, 60, 100, 140, 180, 220]
    found_signal_strengths = []
    increment_value = 0
    display = ''
    for instruction in data_lines:
        if search_cycles.__contains__(cycle):
            found_signal_strengths.append(signal_strength)
        signal_strength += increment_value
        display += get_lit_pixel(cycle, signal_strength)
        if instruction == 'noop':
            cycle += 1
            increment_value = 0
        else:
            [_, value] = instruction.split(' ')
            cycle += 1
            display += get_lit_pixel(cycle, signal_strength)
            if search_cycles.__contains__(cycle):
                found_signal_strengths.append(signal_strength)
            cycle += 1
            increment_value = int(value)

    print('\n'.join([display[i:i + 40] for i in range(0, len(display), 40)]))
    print(sum([modifier * strength for (strength, modifier) in zip(found_signal_strengths, search_cycles)]))
