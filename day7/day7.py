import json


def recursively_search_100k_and_below(file_structure_part: dict, found_sizes: list, search_size=100_000):
    part_size = file_structure_part.__getitem__('total_size')
    if part_size < search_size:
        found_sizes.append(part_size)
    for deep_search in file_structure_part.values():
        if isinstance(deep_search, dict):
            recursively_search_100k_and_below(deep_search, found_sizes)
    return found_sizes


def recursively_search_lowest_to_delete_for_30m_free_space(file_structure_part: dict, found_sizes: list,
                                                           free_space: int):
    part_size = file_structure_part.__getitem__('total_size')
    if free_space + part_size >= 30_000_000:
        found_sizes.append(part_size)
    for deep_search in file_structure_part.values():
        if isinstance(deep_search, dict):
            recursively_search_lowest_to_delete_for_30m_free_space(deep_search, found_sizes, free_space)
    return found_sizes


with open('day7.data', 'r') as file:
    data = file.read()
    data_lines = data.split('\n')
    file_struct = {'/': {'total_size': 0}}
    current_directory = []
    for element in data_lines:
        if element.startswith('$ cd'):
            move_dir = element.split('$ cd ')[1]
            if move_dir == '..':
                current_directory.pop()
            else:
                current_directory.append(move_dir)
        elif element.startswith('dir'):
            directory = element.split('dir ')[1]
            sub_dir = file_struct
            for path in current_directory:
                sub_dir = sub_dir.__getitem__(path)
            sub_dir.__setitem__(directory, {'total_size': 0})
        elif element.startswith('$ ls'):
            pass
        else:
            [size, item] = element.split(' ')
            sub_dir = file_struct
            for path in current_directory:
                sub_dir = sub_dir.__getitem__(path)
                dir_size = sub_dir.__getitem__('total_size')
                sub_dir.__setitem__('total_size', int(size) + dir_size)
            sub_dir.__setitem__(item, int(size))

    max_space = 70_000_000
    used_space = file_struct.__getitem__('/').__getitem__('total_size')
    free_space = 70_000_000 - used_space
    print(min(recursively_search_lowest_to_delete_for_30m_free_space(file_struct.__getitem__('/'), [], free_space)))
    print(sum(recursively_search_100k_and_below(file_struct.__getitem__('/'), [])))
    # print(json.dumps(file_struct, indent=4))
