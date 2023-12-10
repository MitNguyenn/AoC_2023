convert = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e',
    }



with open('day1.txt', 'r') as file, open('part2.txt', 'w') as f:        
    #with open('part2.txt', 'w') as f:
    for each in file.readlines():
        for element in convert:
            each = each.replace(element, convert[element])
        f.writelines(each)

        
                
