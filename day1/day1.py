with open('day1.data', 'r') as file:

    data = file.read()
    calories_per_elf = [calories.split('\n') for calories in data.split('\n\n')]
    total_calories_per_elf = [sum([int(calorie) for calorie in calories]) for calories in calories_per_elf]
    top3 = sorted(total_calories_per_elf)[-3:]
    print(top3)
    print(top3[0])  # top elf
    print(sum(top3))  # top 3 sum

