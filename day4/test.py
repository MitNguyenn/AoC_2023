save = {'Card 1' : 1,
        'Card 2' : 1,
        'Card 3' : 1,
        'Card 4' : 1,
        'Card 5' : 1,
        'Card 6' : 1}

win = [[41, 48, 83, 86, 17],
       [13 ,32, 20, 16, 61],
       [1, 21, 53, 59, 44],
       [41, 92, 73, 84, 69],
       [87, 83, 26, 28, 32],
       [31, 18, 13, 56 ,73]]

have = [[83, 86,  6, 31, 17,  9, 48, 53],
        [61, 30, 68, 82, 17, 32, 24, 19],
        [69, 82, 63, 72, 16, 21, 14,  1],
        [59, 84, 76, 51, 58,  5, 54, 83],
        [88, 30, 70, 12, 93, 22, 82, 36],
        [74, 77, 10, 23, 35, 67, 36, 11]]

name = ''
for i in range(6):
    count = 0
    for num in win[i]:
        if num in have[i]:
            count += 1
    temp = i
    previous = f'Card {temp + 1}'
    for j in range(count):
        name = f'Card {temp + 2}'
        save[name] += 1 * save[previous]
        temp += 1
sum = 0
for value in save:
    sum += save[value]

print(save)
print(sum)
