import math

instruction = []
node = {}

with open('day8.txt') as file:
    for line in file:
        way = []
        if line.startswith('LLL'):
            for letter in line:
                instruction.append(letter)
        else:
            if line != '\n':
                source, des = line.split(sep = ' = ')
                des = des.replace('\n', '').replace(')', '').replace('(', '')
                l, r = des.split(sep = ', ')
                way.append(l)
                way.append(r)
                node[source] = way
    instruction.remove(instruction[-1])
    
    final = ''
    sum = []
    for one in node:
        if one[-1] == 'A':
            final = one
            step = 0
            while final[-1] != 'Z':
                for each in instruction:
                    if each == 'L':
                        final = node[final][0]            
                    else:
                        final = node[final][1]
                    step += 1
            sum.append(step)
    print(math.lcm(16579, 18827, 19951, 12083, 22199, 17141))

                
        