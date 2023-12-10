with open('day2.txt', 'r') as file:
    sum = 0
    for line in file:
        red = green = blue = 0
        line = line.replace(';', '').replace(',', '').replace('Game', '').replace(':', '').strip().split()
        line = line[1:]
        for i in range(len(line)):
            if line[i].isdigit():
                pass
            else:
                if line[i] == 'green':
                    if int(line[i-1]) > green:
                        green = int(line[i-1])
                elif line[i] == 'blue':
                    if int(line[i-1]) > blue:
                        blue = int(line[i-1])
                else:
                    if int(line[i-1]) > red:
                        red = int(line[i-1])
        sum += red * green * blue
print(sum)
