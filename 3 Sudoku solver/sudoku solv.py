

import sys
sys.setrecursionlimit(20000)

from tkinter import *


# GUI
sudoku_root = Tk()
sudoku_root.title('Sudoku Solver')

#Poi
txt ='a{}{} = Entry(sudoku_root, width=6, borderwidth=6)\n'
txt2 =''
for r in range(1,10):
    for c in range(1,10):
        t = txt
        txt2 += t.format(r,c)

txt2b ='a{}{}.grid(row={}, column={}, columnspan=1, padx=10, pady=10)\n'
txt22b = ''
for r in range(1,10):
    for c in range(1,10):
        tb = txt2b
        txt22b += tb.format(r,c,r,c)

code = txt2 +'\n' + txt22b
exec (code)

def solve():

    to_sol ='''
if val == '':
    row.append(0)
else :
    row.append(int(val))    
'''
    t1='val = a{}{}.get()\n'
    to_sud =[]
    for r in range(1,10):
        row =[]
        for c in range(1,10):
            tb1 = t1
            tb2 = tb1.format(r,c) + to_sol

            exec (tb2)
        to_sud.append(row)

    for rows in to_sud:
        print(rows)

    # Algo
    # Znajduje pozycje w planszy gdzie jest 0 ( zwraca pozycje x,y -> row, col ) )
    def zero_finder(matrix):

        poz = []
        for row in matrix:
            for element in row:
                if element == 0:
                    n = row.index(0)
                    x = matrix.index(row)
                    poz.append(x)
                    poz.append(n)
                    break
            if len(poz) > 0:
                break
        return poz

    # flattuje liste
    def flatten(lista):
        flatted_list = []
        for element in lista:
            for e in element:
                if element != 0:
                    flatted_list.append(e)
        return flatted_list

    # sprawdza jakie liczby mozna wstawic na danym polu
    def numb_finder(poz, matrix):

        if len(poz) == 0:
            return []

        s1 = flatten([matrix[0][0:3], matrix[1][0:3], matrix[2][0:3]])
        s2 = flatten([matrix[0][3:6], matrix[1][3:6], matrix[2][3:6]])
        s3 = flatten([matrix[0][6:], matrix[1][6:], matrix[2][6:]])

        s4 = flatten([matrix[3][0:3], matrix[4][0:3], matrix[5][0:3]])
        s5 = flatten([matrix[3][3:6], matrix[4][3:6], matrix[5][3:6]])
        s6 = flatten([matrix[3][6:], matrix[4][6:], matrix[5][6:]])

        s7 = flatten([matrix[6][0:3], matrix[7][0:3], matrix[8][0:3]])
        s8 = flatten([matrix[6][3:6], matrix[7][3:6], matrix[8][3:6]])
        s9 = flatten([matrix[6][6:], matrix[7][6:], matrix[8][6:]])

        # czyli mamy poz x,y musimy ustalic jakie liczby tam moga byc

        all_numbers = list(range(1, 10))

        forbidden_numbers = []

        # liczby w kolummnach

        for row in matrix:
            forbidden_numbers.append([row[poz[1]]])
        # liczby w row

        forbidden_numbers.append(matrix[poz[0]])
        # dla rows < 3
        if poz[0] < 3:
            if poz[1] < 3:
                forbidden_numbers.append(s1)
            elif poz[1] >= 3 and poz[1] < 6:
                forbidden_numbers.append(s2)
            elif poz[1] >= 6:
                forbidden_numbers.append(s3)

        elif poz[0] >= 3 and poz[0] < 6:
            if poz[1] < 3:
                forbidden_numbers.append(s4)
            elif poz[1] >= 3 and poz[1] < 6:
                forbidden_numbers.append(s5)
            elif poz[1] >= 6:
                forbidden_numbers.append(s6)

        elif poz[0] >= 6:
            if poz[1] < 3:
                forbidden_numbers.append(s7)
            elif poz[1] >= 3 and poz[1] < 6:
                forbidden_numbers.append(s8)
            elif poz[1] >= 6:
                forbidden_numbers.append(s9)

        # znajdowanie liczb
        end_numb = []
        forbidden_numbers = flatten(forbidden_numbers)
        for number in all_numbers:
            if number not in forbidden_numbers:
                end_numb.append(number)

        return end_numb

    # wstawianie na okreslonej pozycji
    def ws(poz, num, matrix):
        new_matrix = matrix
        new_matrix[poz[0]][poz[1]] = num
        return new_matrix

    history = []

    def sudoku_solver(matrix):

        poz = zero_finder(matrix)
        numbers = numb_finder(poz, matrix)

        if len(numbers) == 0 and len(poz) == 0:
            print('Finished')
            for e in matrix:
                print(e)

        elif len(numbers) == 0 and len(poz) != 0:

            old = history[-1]
            old_ma = old[0]
            old_poz = old[1]
            old_nu = old[2]
            old_tr = old[3]

            if len(old_nu) > 1:

                if old_ma[old_poz[0]][old_poz[1]] == old_nu[0]:
                    old_tr.append(old_nu[0])
                    old_nu.remove(old_nu[0])
                    old_ma[old_poz[0]][old_poz[1]] = old_nu[0]
                    his = [old_ma, old_poz, old_nu, old_tr]
                    history.append(his)

                    sudoku_solver(old_ma)

            elif len(old_nu) == 1:
                p_x = history[-1][1][0]
                p_y = history[-1][1][1]
                history[-1][0][p_x][p_y] = 0
                history.remove(history[-1])
                old_nu2 = history[-1][2]
                if len(old_nu2) == 1:
                    while True:
                        p_x = history[-1][1][0]
                        p_y = history[-1][1][1]
                        history[-1][0][p_x][p_y] = 0
                        history.remove(history[-1])

                        if len(history[-1][2]) != 1:
                            break

                old_2 = history[-1]
                old_ma2 = old_2[0]
                old_poz2 = old_2[1]
                old_nu2 = old_2[2]
                old_tr2 = old_2[3]

                if old_ma2[old_poz2[0]][old_poz2[1]] == old_nu2[0]:
                    old_tr2.append(old_nu2[0])
                    old_nu2.remove(old_nu2[0])
                    old_ma2[old_poz2[0]][old_poz2[1]] = old_nu2[0]
                    his = [old_ma2, old_poz2, old_nu2, old_tr2]
                    history.append(his)

                    sudoku_solver(old_ma2)
        else:

            history_a1 = [matrix, poz, numbers, []]
            history.append(history_a1)
            new = ws(poz, numbers[0], matrix)

            sudoku_solver(new)

    sudoku_solver(to_sud)


solve = Button(sudoku_root, text='Solve', padx=40, pady=20, command=solve)
solve.grid(row=0, column=10)


sudoku_root.mainloop()