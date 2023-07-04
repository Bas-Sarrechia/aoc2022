with open('day6.data', 'r') as file:
    data = file.read()
    search_len = 4
    for idx in range(len(data)):
        if len(set(data[idx:idx + search_len])) == search_len:
            print(idx+search_len)
            break
