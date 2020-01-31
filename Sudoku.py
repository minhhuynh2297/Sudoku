import tkinter as tk
import copy

root = tk.Tk()
root.title("Sudoku")
root.minsize(450, 575)

display_board = [[tk.Entry(root, font="Calibri 18", justify=tk.CENTER) for i in range(9)] for j in range(9)]
board_row, board_column = [['' for i in range(9)] for j in range(9)], [[0 for i in range(9)] for j in range(9)]
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
rp, cp, bp = [[1, 2, 3, 4, 5, 6, 7, 8, 9] for i in range(9)], \
             [[1, 2, 3, 4, 5, 6, 7, 8, 9] for i in range(9)], \
             [[1, 2, 3, 4, 5, 6, 7, 8, 9] for i in range(9)]

ap = [[[1, 2, 3, 4, 5, 6, 7, 8, 9] for i in range(9)] for j in range(9)]


def check(): # removes possibility
    for i in range(9):
        for j in range(9):
            if len(display_board[i][j].get()) is 1:
                ap[i][j].clear()
                entry_num = int(display_board[i][j].get())
                if entry_num in rp[j] and entry_num in cp[i]:
                    rp[j].remove(entry_num)
                    cp[i].remove(entry_num)
                if i in range(0, 3) and j in range(0, 3):   # top left
                    if entry_num in bp[0]:
                        bp[0].remove(entry_num)
                elif i in range(3, 6) and j in range(0, 3):  # top mid
                    if entry_num in bp[1]:
                        bp[1].remove(entry_num)
                elif i in range(6, 9) and j in range(0, 3):  # top right
                    if entry_num in bp[2]:
                        bp[2].remove(entry_num)
                elif i in range(0, 3) and j in range(3, 6) :  # mid left
                    if entry_num in bp[3]:
                        bp[3].remove(entry_num)
                elif i in range(3, 6) and j in range(3, 6) :  # mid mid
                    if entry_num in bp[4]:
                        bp[4].remove(entry_num)
                elif i in range(6, 9) and j in range(3, 6) :  # mid right
                    if entry_num in bp[5]:
                        bp[5].remove(entry_num)
                elif i in range(0, 3) and j in range(6, 9):   # bot left
                    if entry_num in bp[6]:
                        bp[6].remove(entry_num)
                elif i in range(3, 6) and j in range(6, 9) :  # bot mid
                    if entry_num in bp[7]:
                        bp[7].remove(entry_num)
                elif i in range(6, 9) and j in range(6, 9) :  # bot right
                    if entry_num in bp[8]:
                        bp[8].remove(entry_num)


def option_reducer(): # remove possibility of number if row, column, block has it
    row = takenOptions(rp)
    col = takenOptions(cp)
    blk = takenOptions(bp)
    r, c, b = [[] for i in range(9)], [[] for i in range(9)], [[] for i in range(9)]
    for i in range(0, 3):
        for j in range(0, 3):
            for item in row[j]:
                if item in ap[i][j]:
                    ap[i][j].remove(item)
            for item in col[i]:
                if item in ap[i][j]:
                    ap[i][j].remove(item)
            for item in blk[0]:
                if item in ap[i][j]:
                    ap[i][j].remove(item)
            r[j].append()
    
        for j in range(3, 6) :
            for item in row[j] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)
            for item in col[i] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)
            for item in blk[3] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)

        for j in range(6, 9) :
            for item in row[j] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)
            for item in col[i] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)
            for item in blk[6] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)

    for i in range(3, 6):

        for j in range(0, 3):
            for item in row[j]:
                if item in ap[i][j]:
                    ap[i][j].remove(item)
            for item in col[i]:
                if item in ap[i][j]:
                    ap[i][j].remove(item)
            for item in blk[1]:
                if item in ap[i][j]:
                    ap[i][j].remove(item)

        for j in range(3, 6) :
            for item in row[j] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)
            for item in col[i] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)
            for item in blk[4] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)

        for j in range(6, 9) :
            for item in row[j] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)
            for item in col[i] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)
            for item in blk[7] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)

    for i in range(6, 9):

        for j in range(0, 3):
            for item in row[j]:
                if item in ap[i][j]:
                    ap[i][j].remove(item)
            for item in col[i]:
                if item in ap[i][j]:
                    ap[i][j].remove(item)
            for item in blk[2]:
                if item in ap[i][j]:
                    ap[i][j].remove(item)

        for j in range(3, 6):
            for item in row[j]:
                if item in ap[i][j]:
                    ap[i][j].remove(item)

            for item in col[i]:
                if item in ap[i][j]:
                    ap[i][j].remove(item)

            for item in blk[5]:
                if item in ap[i][j]:
                    ap[i][j].remove(item)

        for j in range(6, 9) :
            for item in row[j] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)

            for item in col[i] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)

            for item in blk[8] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)



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
    check()
    option_reducer()
    print(ap[4][0], ap[]
    print(bp[1])
  #  solve()

# finished methods
def initialize() :
    for i in range(9) :
        for j in range(9) :
            display_board[i][j].delete(0, 'end')
            display_board[i][j].place(height=50, width=50, x=i * 50, y=j * 50)

def takenOptions(rcb):
    return [list(numbers.difference(set(rcb[i]))) for i in range(9)]

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

def save() :  # saves current changes
    for i in range(9) :
        for j in range(9) :
            board_column[i][j] = display_board[i][j].get()
            board_row[j][i] = display_board[i][j].get()
    blocks = [[board_row[i][j] for i in range(0, 3) for j in range(0, 3)],  # top left
              [board_row[i][j] for i in range(3, 6) for j in range(0, 3)],  # top middle
              [board_row[i][j] for i in range(6, 9) for j in range(0, 3)],  # top right
              [board_row[i][j] for i in range(0, 3) for j in range(3, 6)],  # middle left
              [board_row[i][j] for i in range(3, 6) for j in range(3, 6)],  # middle middle
              [board_row[i][j] for i in range(6, 9) for j in range(3, 6)],  # middle right
              [board_row[i][j] for i in range(0, 3) for j in range(6, 9)],  # bottom left
              [board_row[i][j] for i in range(3, 6) for j in range(6, 9)],  # bottom middle
              [board_row[i][j] for i in range(6, 9) for j in range(6, 9)]]  # bottom right
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
