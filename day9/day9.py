def last(lst):
    holder = []
    for i in range(len(lst)-1):
        holder.append(int(lst[i+1])-int(lst[i]))
        
    if all(number == 0 for number in holder):
        return (holder[-1])
    else:
        return holder[-1] + last(holder)
        
with open('day9.txt') as file:
    sum = 0
    file = file.read().strip().split(sep = '\n')
    
    for line in file:
        line = line.split()
        sum += last(line) + int(line[-1])
print(sum)
    


            