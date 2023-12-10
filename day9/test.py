def last(lst):
    holder = []
    for i in range(len(lst) - 1):
        holder.append(int(lst[i + 1]) - int(lst[i]))

    if all(number == 0 for number in holder):
        return holder[-1]
    else:
        return holder[-1] + last(holder)

# Assuming the input sequences are stored in a list named 'sequences'
sequences = [
    "0 3 6 9 12 15",
    "1 3 6 10 15 21",
    "10 13 16 21 30 45"
]

total_sum = 0

for line in sequences:
    temp = line.split()
    total_sum += last(temp)

print(total_sum)