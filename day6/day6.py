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
        
    vic = 1
    
    for i in range(len(time)):
        record = int(distance[i])
        moment = int(time[i])
        travel = 0
        temp = 0
        count = 0
        
        while moment >= 0:
            travel = moment * temp
            if travel > record:
                count += 1
            moment -= 1
            temp += 1
        vic *= count
            
                    
    print(count,vic)