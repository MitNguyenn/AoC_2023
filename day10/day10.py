with open('day10.txt') as file:
    sudoku = []
    for line in file:
        line = line.strip()
        row = []
        for each in line:
            row.append(each)
        sudoku.append(line)
        
place = []
x = y = 0
for i in range(len(sudoku[0])):
    for j in range(len(sudoku)):
        if sudoku[i][j] == 'S':
            x = i + 1
            y = j - 1
            break
            
starting = (x ,y + 1)
ending = (x, y)
step = 2

while True:
    step += 1
    cell = sudoku[x][y]
    if cell == "L":
        if ending[0]  == starting[0]:
            x -= 1
        else:
            y += 1
    elif cell == 'J':
        if ending[0] > starting[0]:
            y -= 1
        else:
            x -= 1
    elif cell == 'F':
        if ending[0] < starting[0]:
            y += 1
        else:
            x += 1
    elif cell == '7':
        if ending[1] > starting[1]:
            x += 1
        else:
            y -= 1
    elif cell == '|':
        if ending[0] > starting[0]:
            x += 1
        else:
            x -= 1
    elif cell == '-':
        if ending[1] > starting[1]:
            y += 1
        else:
            y -= 1         
    starting = ending       
    ending = (x, y)
    
    if sudoku[x][y] == 'S':
        break
    
print(step//2)