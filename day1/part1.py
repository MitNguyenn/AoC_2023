new = ''
sum = 0


with open (input('Please enter your file name: '), 'r') as file:
    for line in file:
        for char in line:
            if char.isdigit():
                new += char
                break
        for letter in line[::-1]:
            if letter.isdigit():
                new += letter
                break
        sum += int(new)
        new = ''
print(sum)
