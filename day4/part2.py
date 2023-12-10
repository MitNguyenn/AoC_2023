with open('day4.txt') as file:
    save = {}
    WIN =[]
    HAVE = []
    for line in file:
        name, card = line.split(sep=':')
        for _ in range(1,199):
            bored = f'Card {_}'
            if bored not in save:
                save[bored] = 1

        win, have = card.strip().split(sep = '|')
        WIN.append(win.split())
        HAVE.append(have.split())



    name = ""
    for i in range(198):
        count = 0
        for num in WIN[i]:
            if num in HAVE[i]:
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
    print(sum)
