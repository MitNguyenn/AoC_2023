RED = 12
GREEN = 13
BLUE = 14

sum = 0
hold = []
check = True

with open('day2.txt', 'r') as file:
    for line in file:
        line = line.replace(';', '').replace(',', '').replace('Game', '').replace(':', '').strip().split()
        for i in range(len(line[1:])):
            if line[i].isdigit():
                pass
            else:
                if line[i] == 'green':
                    if int(line[i-1]) > GREEN:
                        check = False
                        break
                elif line[i] == 'blue':
                    if int(line[i-1]) > BLUE:
                        check = False
                        break
                else:
                    if int(line[i-1]) > RED:
                        check = False
                        break
        if check == True:
            sum += int(line[0])
        check = True
print(sum)

