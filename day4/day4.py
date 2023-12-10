with open('day4.txt') as file:
    point = 0
    for line in file:
        win, have = line[10:].strip().split(sep = '|')
        count = 0
        for element in win.split():
            if element in have.split():
                count += 1
        if count > 0:
            point += 2**(count - 1)
    print(point)
