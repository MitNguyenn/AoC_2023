sudoku = []
sudoku2 = []
sudoku3 = []
empty = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
with open('write.txt', 'r') as file:
    
    #expand row
    for line in file:
        row = []
        if '#' in line:
            for each in line.strip():
                row.append(each)
            sudoku.append(row)
        elif line != '\n':
            sudoku.append(empty)
 
    #roll the sudoku
    for m in range(len(sudoku[0])):
        row = []
        for n in range(len(sudoku)):
            row.append(sudoku[n][m])
        sudoku2.append(''.join(row))

    #expand the column
    for some in sudoku2:
        row = []
        if '#' in some:
            for char in some:
                row.append(char)
            sudoku3.append(row)
        else:
            sudoku3.append(empty)
    
    for what in sudoku3:
        print(what)
   
    x = []
    y = []

    for i in range(len(sudoku3)):
        for j in range(len(sudoku3[0])):
            if sudoku3[i][j] == '#':
                x.append(j)
                y.append(i)
    print(x, y)
    sum = 0

    for a in range(len(x)):
        for b in range(a + 1, len(x)):
            sum += abs(x[a] - x[b])
            if x[a] < x[b]:
                for expand in range(x[a], x[b]):
                    if sudoku3[0][expand] == 'A':
                        sum += 9
            elif x[a] > x[b]:
                for expand in range(x[b], x[a]):
                    if sudoku3[0][expand] == 'A':
                        sum += 9
            else:
                sum += 0
    for c in range(len(y)):
        for d in range(c + 1, len(y)):
            sum += abs(y[c]- y[d])
            if y[c] < y[d]:
                for expansion in range(y[c], y[d]):
                    if sudoku3[expansion][0] == "A":
                        sum += 9
            elif y[c] > y[d]:
                for expansion in range(y[d], y[c]):
                    if sudoku3[expansion][0] == 'A':
                        sum += 9
            else:
                sum += 0
                
    print(sum)