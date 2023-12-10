with open('day6.txt') as file:
    time = []
    distance = []
    for line in file:
        line = line.split()
        if "Time:" in line:
            time = line
        else:
            distance = line
        line.remove(line[0])

    displacement = moment = 1
    
    moment = int(''.join(time))
    travel = int(''.join(distance))
    
    
    
    temp = count = 0
    while moment >= 0:
        displacement = moment * temp
        if displacement > travel:
            temp1 = temp
            temp2 = moment
        moment -= 1
        temp += 1
    print(temp1-temp2 +1)
    