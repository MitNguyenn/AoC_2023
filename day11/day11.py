sudoku = []
sudoku2 = []
sudoku3 = []
empty = ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
empty2 = ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
count = 0
with open('day11.txt', 'r') as file:
    for line in file:
        row = []
        if '#' in line:
            for each in line.strip():
                row.append(each)
            sudoku.append(row)
        else:
            sudoku.append(empty)
            sudoku.append(empty)

    print(len(sudoku))

    for m in range(len(sudoku[0])):
        row = []
        for n in range(len(sudoku)):
            row.append(sudoku[n][m])
        sudoku2.append(''.join(row))
    
    for some in sudoku2:
        row = []
        if '#' in some:
            for char in some:
                row.append(char)
            sudoku3.append(row)
        else:
            sudoku3.append(empty2)
            sudoku3.append(empty2)
        
            

y = []
x = []

for i in range(len(sudoku3)):
    for j in range(len(sudoku3[0])):
        if sudoku3[i][j] == '#':
            x.append(i)
            y.append(j)

sum = 0

for a in range(len(x)):
    for b in range(a + 1, len(x)):
        sum += abs(x[a] - x[b])
for c in range(len(y)):
    for d in range(c + 1, len(y)):
        sum += abs(y[c]- y[d])
        
print(sum)