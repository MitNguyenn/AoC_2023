with open('day5.txt') as file:
    #get the seed number
    for first in file:
        rid, num = first.split(sep = ": ")
        num = num.split()        
        break
    
    #map the seed to the corresponding
position = 10000000000000
go = True
for i in range(len(num)):
    temp = int(num[i])
    with open('day5.txt') as file:
        for line in file:
            if go:
                if line[0].isdigit():
                    line = line.split()
                    if (temp >= int(line[1])) and (temp <= (int(line[1]) + int(line[2]))):
                        temp = temp - int(line[1]) + int(line[0])
                        go = False
            elif line[0].isalpha():
                go = True
                
        if temp < position:
            position = temp
    print(num[i], temp)
print(position)
                    
