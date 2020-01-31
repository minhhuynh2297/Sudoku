import tkinter as tk
import copy

root = tk.Tk()
root.title("Sudoku")
root.minsize(450, 575)

display_board = [[tk.Entry(root, font="Calibri 18", justify=tk.CENTER) for i in range(9)] for j in range(9)]
ap = [[[1, 2, 3, 4, 5, 6, 7, 8, 9] for i in range(9)] for j in range(9)]
rp = [[copy.copy(ap[i][y]) for i in range(9)] for y in range(9)]  # references to ap rows
cp = [[copy.copy(ap[y][i]) for i in range(9)] for y in range(9)]  # references to ap columns
bp = [
        [copy.copy(ap[i][y]) for i in range(0, 3) for y in range(0, 3)],
        [copy.copy(ap[i][y]) for i in range(3, 6) for y in range(0, 3)],
        [copy.copy(ap[i][y]) for i in range(6, 9) for y in range(0, 3)],
        [copy.copy(ap[i][y]) for i in range(0, 3) for y in range(3, 6)],
        [copy.copy(ap[i][y]) for i in range(3, 6) for y in range(3, 6)],
        [copy.copy(ap[i][y]) for i in range(6, 9) for y in range(3, 6)],
        [copy.copy(ap[i][y]) for i in range(0, 3) for y in range(6, 9)],
        [copy.copy(ap[i][y]) for i in range(3, 6) for y in range(6, 9)],
        [copy.copy(ap[i][y]) for i in range(6, 9) for y in range(6, 9)]
     ]

def check():
    for i in range(9):
        for j in range(9):
            if len(display_board[i][j].get()) is 1:
                entry_num = int(display_board[i][j].get())
                for z in range(9):
                    if entry_num in rp[j][z] and entry_num in cp[i][z]:
                        rp[j][z].remove(entry_num)
                        cp[i][z].remove(entry_num)
                if i in range(0, 3) and j in range(0, 3):   # top left
                    for z in range(9) :
                        if entry_num in bp[0][z]:
                            bp[0][z].remove(entry_num)
                elif i in range(3, 6) and j in range(0, 3):  # top mid
                    for z in range(9) :
                        if entry_num in bp[1][z]:
                            bp[1][z].remove(entry_num)
                elif i in range(6, 9) and j in range(0, 3):  # top right
                    for z in range(9) :
                        if entry_num in bp[2][z]:
                            bp[2][z].remove(entry_num)
                elif i in range(0, 3) and j in range(3, 6) :  # mid left
                    for z in range(9) :
                        if entry_num in bp[3][z]:
                            bp[3][z].remove(entry_num)
                elif i in range(3, 6) and j in range(3, 6) :  # mid mid
                    for z in range(9) :
                        if entry_num in bp[4][z]:
                            bp[4][z].remove(entry_num)
                elif i in range(6, 9) and j in range(3, 6) :  # mid right
                    for z in range(9) :
                        if entry_num in bp[5][z]:
                            bp[5][z].remove(entry_num)
                elif i in range(0, 3) and j in range(6, 9):   # bot left
                    for z in range(9) :
                        if entry_num in bp[6][z]:
                            bp[6][z].remove(entry_num)
                elif i in range(3, 6) and j in range(6, 9) :  # bot mid
                    for z in range(9) :
                        if entry_num in bp[7][z]:
                            bp[7][z].remove(entry_num)
                elif i in range(6, 9) and j in range(6, 9) :  # bot right
                    for z in range(9) :
                        if entry_num in bp[8][z]:
                            bp[8][z].remove(entry_num)



def solve():
    in_order = [[] for i in range(10)]
    for i in range(9):
        for j in range(9):
            in_order[len(ap[i][j])].append(tuple((i, j)))
    if len(in_order[0]) is 81:
        display.config(text="FINISH")
        return
    for pair in in_order[1]:
        i, j = pair[0], pair[1]
        number = ap[i][j].pop(0)
        display_board[i][j].insert(0, number)
   # check()
    print(ap[0][0])
    print(rp[0][0])

  #  solve()

# finished methods
def initialize() :
    for i in range(9) :
        for j in range(9) :
            display_board[i][j].delete(0, 'end')
            display_board[i][j].place(height=50, width=50, x=i * 50, y=j * 50)

def takenOptions(rcb):
    return [list({1, 2, 3, 4, 5, 6, 7, 8, 9}.difference(set(rcb[i]))) for i in range(9)]

def minimumSize(rcb):
    minimum = 9
    min_list = []
    for i in rcb:
        if len(i) < minimum and len(i) is not 0:
            minimum = len(i)
            min_list = i
    return min_list

def start():
    for i in range(9) :
        for j in range(9):
            if len(display_board[i][j].get()) is 1:
                display_board[i][j].config(state=tk.DISABLED)
    save()

def save() :  # saves current
    display.config(text="Saved")

starter = tk.Button(root, text="Start", command=start)
starter.place(x=50, y=525)

clearer = tk.Button(root, text="Clear", command=initialize)
clearer.place(x=100, y=525)

checker = tk.Button(root, text="Check", command=check)
checker.place(x=50, y=475)

solver = tk.Button(root, text="Solve", command=solve)
solver.place(x=100, y=475)

display = tk.Label(root)
display.place(x=300, y=500)

display.config(text="Input Your Puzzle")
initialize()
root.mainloop()
