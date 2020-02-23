import tkinter as tk
import itertools as it


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


def check() :  # removes possibility
    for i in range(9) :
        for j in range(9) :
            if len(display_board[i][j].get()) is 1 :
                ap[i][j].clear()
                entry_num = int(display_board[i][j].get())
                if entry_num in rp[j] and entry_num in cp[i] :
                    rp[j].remove(entry_num)
                    cp[i].remove(entry_num)
                if i in range(0, 3) and j in range(0, 3) :  # top left
                    if entry_num in bp[0] :
                        bp[0].remove(entry_num)
                elif i in range(3, 6) and j in range(0, 3) :  # top mid
                    if entry_num in bp[1] :
                        bp[1].remove(entry_num)
                elif i in range(6, 9) and j in range(0, 3) :  # top right
                    if entry_num in bp[2] :
                        bp[2].remove(entry_num)
                elif i in range(0, 3) and j in range(3, 6) :  # mid left
                    if entry_num in bp[3] :
                        bp[3].remove(entry_num)
                elif i in range(3, 6) and j in range(3, 6) :  # mid mid
                    if entry_num in bp[4] :
                        bp[4].remove(entry_num)
                elif i in range(6, 9) and j in range(3, 6) :  # mid right
                    if entry_num in bp[5] :
                        bp[5].remove(entry_num)
                elif i in range(0, 3) and j in range(6, 9) :  # bot left
                    if entry_num in bp[6] :
                        bp[6].remove(entry_num)
                elif i in range(3, 6) and j in range(6, 9) :  # bot mid
                    if entry_num in bp[7] :
                        bp[7].remove(entry_num)
                elif i in range(6, 9) and j in range(6, 9) :  # bot right
                    if entry_num in bp[8] :
                        bp[8].remove(entry_num)


def block_reducer(b_num, reduct) :
    for i in range(1, 10) :
        fst = -1
        snd = -1
        count = 0
        for j in range(9) :
            if count > 2 :
                break
            if i in reduct[j] :
                if count is 0 :
                    fst = j
                else :
                    snd = j
                count = count + 1
        if count is 1 :
            one_option(b_num, reduct, fst, snd, i)
        elif count is 2 :
            two_options(b_num, reduct, fst, snd, i)
        only_two_options(b_num, reduct)


def reducer() :  # remove possibility of number if row, column, block has it
    row = takenOptions(rp)
    col = takenOptions(cp)
    blk = takenOptions(bp)
    b = [[] for i in range(9)]
    for i in range(0, 3) :
        for j in range(0, 3) :
            for item in row[j] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)
            for item in col[i] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)
            for item in blk[0] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)
            b[0].append(ap[i][j])
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
            b[3].append(ap[i][j])
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
            b[6].append(ap[i][j])

    for i in range(3, 6) :
        for j in range(0, 3) :
            for item in row[j] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)
            for item in col[i] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)
            for item in blk[1] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)
            b[1].append(ap[i][j])
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
            b[4].append(ap[i][j])

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
            b[7].append(ap[i][j])

    for i in range(6, 9) :
        for j in range(0, 3) :
            for item in row[j] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)
            for item in col[i] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)
            for item in blk[2] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)
            b[2].append(ap[i][j])

        for j in range(3, 6) :
            for item in row[j] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)
            for item in col[i] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)
            for item in blk[5] :
                if item in ap[i][j] :
                    ap[i][j].remove(item)
            b[5].append(ap[i][j])

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
            b[8].append(ap[i][j])

    for i in range(9) :
        block_reducer(i, b[i])


def solve() :
    #print( "######################################################################################################################################")
    in_order = [[] for i in range(10)]
    check()
    reducer()
    for i in range(9) :
       for j in range(9) :
            print(i, ", ", j, ": ", ap[i][j])

    for i in range(9) :
        for j in range(9) :
            in_order[len(ap[i][j])].append(tuple((i, j)))
   # for i in range(9):
    #    print(in_order[i])
    if len(in_order[0]) is 81 :
        display.config(text="FINISH")
        return
    for pair in in_order[1] :
        i, j = pair[0], pair[1]
        number = ap[i][j].pop(0)
        display_board[i][j].insert(0, number)
    #solve()




# finished methods
def initialize() :
    for i in range(9) :
        for j in range(9) :
            display_board[i][j].delete(0, 'end')
            display_board[i][j].place(height=50, width=50, x=i * 50, y=j * 50)


def takenOptions(rcb) :
    return [list(numbers.difference(set(rcb[i]))) for i in range(9)]


def minimumSize(rcb) :
    minimum = 9
    min_list = []
    for i in rcb :
        if len(i) < minimum and len(i) is not 0 :
            minimum = len(i)
            min_list = i
    return min_list


def start() :
    for i in range(9) :
        for j in range(9) :
            if len(display_board[i][j].get()) is 1 :
                display_board[i][j].config(state=tk.DISABLED)

def one_option(b_num, reduct, fst, snd, i):
    if b_num is 0 :
        for n in range(0, 3) :
            for m in range(0, 3) :
                if i in ap[n][m] :
                    ap[n][m].clear()
                    display_board[n][m].insert(0, i)
                    return
    elif b_num is 1 :
        for n in range(3, 6) :
            for m in range(0, 3) :
                if i in ap[n][m] :
                    ap[n][m].clear()
                    display_board[n][m].insert(0, i)
                    return
    elif b_num is 2 :
        for n in range(6, 9) :
            for m in range(0, 3) :
                if i in ap[n][m] :
                    ap[n][m].clear()
                    display_board[n][m].insert(0, i)
                    return
    elif b_num is 3 :
        for n in range(0, 3) :
            for m in range(3, 6) :
                if i in ap[n][m] :
                    ap[n][m].clear()
                    display_board[n][m].insert(0, i)
                    return
    elif b_num is 4 :
        for n in range(3, 6) :
            for m in range(3, 6) :
                if i in ap[n][m] :
                    ap[n][m].clear()
                    display_board[n][m].insert(0, i)
                    return
    elif b_num is 5 :
        for n in range(6, 9) :
            for m in range(3, 6) :
                if i in ap[n][m] :
                    ap[n][m].clear()
                    display_board[n][m].insert(0, i)
                    return
    elif b_num is 6 :
        for n in range(0, 3) :
            for m in range(6, 9) :
                if i in ap[n][m] :
                    ap[n][m].clear()
                    display_board[n][m].insert(0, i)
                    return
    elif b_num is 7 :
        for n in range(3, 6) :
            for m in range(6, 9) :
                if i in ap[n][m] :
                    ap[n][m].clear()
                    display_board[n][m].insert(0, i)
                    return
    elif b_num is 8 :
        for n in range(6, 9) :
            for m in range(6, 9) :
                if i in ap[n][m] :
                    ap[n][m].clear()
                    display_board[n][m].insert(0, i)
                    return

def two_options(b_num, reduct, fst, snd, i):
    if (fst, snd) in [(0, 1), (0, 2), (1, 2), (3, 4), (3, 5), (4, 5), (6, 7), (6, 8), (7, 8)] :  # column
        if b_num is 0 :
            if fst is 0 :
                if snd is 1 :
                    for z in range(2, 9) :
                        if i in ap[0][z] :
                            ap[0][z].remove(i)
                elif snd is 2 :
                    if i in ap[0][1] :
                        ap[0][1].remove(i)
                    for z in range(3, 9) :
                        if i in ap[0][z] :
                            ap[0][z].remove(i)
            elif fst is 1 :
                for z in range(3, 9) :
                    if i in ap[0][z] :
                        ap[0][z].remove(i)
            elif fst is 3 :
                if snd is 4 :
                    for z in range(2, 9) :
                        if i in ap[1][z] :
                            ap[1][z].remove(i)
                elif snd is 5 :
                    if i in ap[1][1] :
                        ap[1][1].remove(i)
                    for z in range(3, 9) :
                        if i in ap[1][z] :
                            ap[1][z].remove(i)
            elif fst is 4 :
                for z in range(3, 9) :
                    if i in ap[1][z] :
                        ap[1][z].remove(i)
            elif fst is 6 :
                if snd is 7 :
                    for z in range(2, 9) :
                        if i in ap[2][z] :
                            ap[2][z].remove(i)
                elif snd is 8 :
                    if i in ap[2][1] :
                        ap[2][1].remove(i)
                    for z in range(3, 9) :
                        if i in ap[2][z] :
                            ap[2][z].remove(i)
            elif fst is 7 :
                for z in range(3, 9) :
                    if i in ap[2][z] :
                        ap[2][z].remove(i)
        elif b_num is 1 :
            if fst is 0 :
                if snd is 1 :
                    for z in range(2, 9) :
                        if i in ap[3][z] :
                            ap[3][z].remove(i)
                elif snd is 2 :
                    if i in ap[3][1] :
                        ap[3][1].remove(i)
                    for z in range(3, 9) :
                        if i in ap[3][z] :
                            ap[3][z].remove(i)
            elif fst is 1 :
                for z in range(3, 9) :
                    if i in ap[3][z] :
                        ap[3][z].remove(i)
            elif fst is 3 :
                if snd is 4 :
                    for z in range(2, 9) :
                        if i in ap[4][z] :
                            ap[4][z].remove(i)
                elif snd is 5 :
                    if i in ap[4][1] :
                        ap[4][1].remove(i)
                    for z in range(3, 9) :
                        if i in ap[4][z] :
                            ap[4][z].remove(i)
            elif fst is 4 :
                for z in range(3, 9) :
                    if i in ap[4][z] :
                        ap[4][z].remove(i)
            elif fst is 6 :
                if snd is 7 :
                    for z in range(2, 9) :
                        if i in ap[5][z] :
                            ap[5][z].remove(i)
                elif snd is 8 :
                    if i in ap[5][1] :
                        ap[5][1].remove(i)
                    for z in range(3, 9) :
                        if i in ap[5][z] :
                            ap[5][z].remove(i)
            elif fst is 7 :
                for z in range(3, 9) :
                    if i in ap[5][z] :
                        ap[5][z].remove(i)
        elif b_num is 2 :
            if fst is 0 :
                if snd is 1 :
                    for z in range(2, 9) :
                        if i in ap[6][z] :
                            ap[6][z].remove(i)
                elif snd is 2 :
                    if i in ap[6][1] :
                        ap[6][1].remove(i)
                    for z in range(3, 9) :
                        if i in ap[6][z] :
                            ap[6][z].remove(i)
            elif fst is 1 :
                for z in range(3, 9) :
                    if i in ap[6][z] :
                        ap[6][z].remove(i)
            elif fst is 3 :
                if snd is 4 :
                    for z in range(2, 9) :
                        if i in ap[7][z] :
                            ap[7][z].remove(i)
                elif snd is 5 :
                    if i in ap[7][1] :
                        ap[7][1].remove(i)
                    for z in range(3, 9) :
                        if i in ap[7][z] :
                            ap[7][z].remove(i)
            elif fst is 4 :
                for z in range(3, 9) :
                    if i in ap[7][z] :
                        ap[7][z].remove(i)
            elif fst is 6 :
                if snd is 7 :
                    for z in range(2, 9) :
                        if i in ap[8][z] :
                            ap[8][z].remove(i)
                elif snd is 8 :
                    if i in ap[8][1] :
                        ap[8][1].remove(i)
                    for z in range(3, 9) :
                        if i in ap[8][z] :
                            ap[8][z].remove(i)
            elif fst is 7 :
                for z in range(3, 9) :
                    if i in ap[8][z] :
                        ap[8][z].remove(i)
        elif b_num is 3 :
            if fst is 0 :
                for z in range(0, 3) :
                    if i in ap[0][z] :
                        ap[0][z].remove(i)
                if snd is 1 :
                    for z in range(5, 9) :
                        if i in ap[0][z] :
                            ap[0][z].remove(i)
                elif snd is 2 :
                    if i in ap[0][4] :
                        ap[0][4].remove(i)
                    for z in range(6, 9) :
                        if i in ap[0][z] :
                            ap[0][z].remove(i)
            elif fst is 1 :
                for z in it.chain(range(0, 4), range(6, 9)) :
                    if i in ap[0][z] :
                        ap[0][z].remove(i)
            elif fst is 3 :
                for z in range(0, 3) :
                    if i in ap[1][z] :
                        ap[1][z].remove(i)
                if snd is 4 :
                    for z in range(5, 9) :
                        if i in ap[1][z] :
                            ap[1][z].remove(i)
                elif snd is 5 :
                    if i in ap[1][4] :
                        ap[1][4].remove(i)
                    for z in range(6, 9) :
                        if i in ap[1][z] :
                            ap[1][z].remove(i)
            elif fst is 4 :
                for z in it.chain(range(0, 4), range(6, 9)) :
                    if i in ap[1][z] :
                        ap[1][z].remove(i)
            elif fst is 6 :
                for z in range(0, 3) :
                    if i in ap[2][z] :
                        ap[2][z].remove(i)
                if snd is 7 :
                    for z in range(5, 9) :
                        if i in ap[2][z] :
                            ap[2][z].remove(i)
                elif snd is 8 :
                    if i in ap[2][4] :
                        ap[2][4].remove(i)
                    for z in range(6, 9) :
                        if i in ap[2][z] :
                            ap[2][z].remove(i)
            elif fst is 7 :
                for z in it.chain(range(0, 4), range(6, 9)) :
                    if i in ap[2][z] :
                        ap[2][z].remove(i)
        elif b_num is 4 :
            if fst is 0 :
                for z in range(0, 3) :
                    if i in ap[3][z] :
                        ap[3][z].remove(i)
                if snd is 1 :
                    for z in range(5, 9) :
                        if i in ap[3][z] :
                            ap[3][z].remove(i)
                elif snd is 2 :
                    if i in ap[3][4] :
                        ap[3][4].remove(i)
                    for z in range(6, 9) :
                        if i in ap[3][z] :
                            ap[3][z].remove(i)
            elif fst is 1 :
                for z in it.chain(range(0, 4), range(6, 9)) :
                    if i in ap[3][z] :
                        ap[3][z].remove(i)
            elif fst is 3 :
                for z in range(0, 3) :
                    if i in ap[4][z] :
                        ap[4][z].remove(i)
                if snd is 4 :
                    for z in range(5, 9) :
                        if i in ap[4][z] :
                            ap[4][z].remove(i)
                elif snd is 5 :
                    if i in ap[4][4] :
                        ap[4][4].remove(i)
                    for z in range(6, 9) :
                        if i in ap[4][z] :
                            ap[4][z].remove(i)
            elif fst is 4 :
                for z in it.chain(range(0, 4), range(6, 9)) :
                    if i in ap[4][z] :
                        ap[4][z].remove(i)
            elif fst is 6 :
                for z in range(0, 3) :
                    if i in ap[5][z] :
                        ap[5][z].remove(i)
                if snd is 7 :
                    for z in range(5, 9) :
                        if i in ap[5][z] :
                            ap[5][z].remove(i)
                elif snd is 8 :
                    if i in ap[5][4] :
                        ap[5][4].remove(i)
                    for z in range(6, 9) :
                        if i in ap[5][z] :
                            ap[5][z].remove(i)
            elif fst is 7 :
                for z in it.chain(range(0, 4), range(6, 9)) :
                    if i in ap[5][z] :
                        ap[5][z].remove(i)
        elif b_num is 5 :
            if fst is 0 :
                for z in range(0, 3) :
                    if i in ap[6][z] :
                        ap[6][z].remove(i)
                if snd is 1 :
                    for z in range(5, 9) :
                        if i in ap[6][z] :
                            ap[6][z].remove(i)
                elif snd is 2 :
                    if i in ap[6][4] :
                        ap[6][4].remove(i)
                    for z in range(6, 9) :
                        if i in ap[6][z] :
                            ap[6][z].remove(i)
            elif fst is 1 :
                for z in it.chain(range(0, 4), range(6, 9)) :
                    if i in ap[6][z] :
                        ap[6][z].remove(i)
            elif fst is 3 :
                for z in range(0, 3) :
                    if i in ap[7][z] :
                        ap[7][z].remove(i)
                if snd is 4 :
                    for z in range(5, 9) :
                        if i in ap[7][z] :
                            ap[7][z].remove(i)
                elif snd is 5 :
                    if i in ap[7][4] :
                        ap[7][4].remove(i)
                    for z in range(6, 9) :
                        if i in ap[7][z] :
                            ap[7][z].remove(i)
            elif fst is 4 :
                for z in it.chain(range(0, 4), range(6, 9)) :
                    if i in ap[7][z] :
                        ap[7][z].remove(i)
            elif fst is 6 :
                for z in range(0, 3) :
                    if i in ap[8][z] :
                        ap[8][z].remove(i)
                if snd is 7 :
                    for z in range(5, 9) :
                        if i in ap[8][z] :
                            ap[8][z].remove(i)
                elif snd is 8 :
                    if i in ap[8][4] :
                        ap[8][4].remove(i)
                    for z in range(6, 9) :
                        if i in ap[8][z] :
                            ap[8][z].remove(i)
            elif fst is 7 :
                for z in it.chain(range(0, 4), range(6, 9)) :
                    if i in ap[8][z] :
                        ap[8][z].remove(i)
        elif b_num is 6 :
            if fst is 0 :
                for z in range(0, 6) :
                    if i in ap[0][z] :
                        ap[0][z].remove(i)
                if snd is 1 :
                    if i in ap[0][8] :
                        ap[0][8].remove(i)
                elif snd is 2 :
                    if i in ap[0][7] :
                        ap[0][7].remove(i)
            elif fst is 1 :
                for z in range(0, 7) :
                    if i in ap[0][z] :
                        ap[0][z].remove(i)
            elif fst is 3 :
                for z in range(0, 6) :
                    if i in ap[1][z] :
                        ap[1][z].remove(i)
                if snd is 4 :
                    if i in ap[1][8] :
                        ap[1][8].remove(i)
                elif snd is 5 :
                    if i in ap[1][7] :
                        ap[1][7].remove(i)
            elif fst is 4 :
                for z in range(0, 7) :
                    if i in ap[1][z] :
                        ap[1][z].remove(i)
            elif fst is 6 :
                for z in range(0, 6) :
                    if i in ap[2][z] :
                        ap[2][z].remove(i)
                if snd is 7 :
                    if i in ap[2][8] :
                        ap[2][8].remove(i)
                elif snd is 8 :
                    if i in ap[2][7] :
                        ap[2][7].remove(i)
            elif fst is 7 :
                for z in range(0, 7) :
                    if i in ap[2][z] :
                        ap[2][z].remove(i)
        elif b_num is 7 :
            if fst is 0 :
                for z in range(0, 6) :
                    if i in ap[3][z] :
                        ap[3][z].remove(i)
                if snd is 1 :
                    if i in ap[3][8] :
                        ap[3][8].remove(i)
                elif snd is 2 :
                    if i in ap[3][7] :
                        ap[3][7].remove(i)
            elif fst is 1 :
                for z in range(0, 7) :
                    if i in ap[3][z] :
                        ap[3][z].remove(i)
            elif fst is 3 :
                for z in range(0, 6) :
                    if i in ap[4][z] :
                        ap[4][z].remove(i)
                if snd is 4 :
                    if i in ap[4][8] :
                        ap[4][8].remove(i)
                elif snd is 5 :
                    if i in ap[4][7] :
                        ap[4][7].remove(i)
            elif fst is 4 :
                for z in range(0, 7) :
                    if i in ap[4][z] :
                        ap[4][z].remove(i)
            elif fst is 6 :
                for z in range(0, 6) :
                    if i in ap[5][z] :
                        ap[5][z].remove(i)
                if snd is 7 :
                    if i in ap[5][8] :
                        ap[5][8].remove(i)
                elif snd is 8 :
                    if i in ap[5][7] :
                        ap[5][7].remove(i)
            elif fst is 7 :
                for z in range(0, 7) :
                    if i in ap[5][z] :
                        ap[5][z].remove(i)
        elif b_num is 8 :
            if fst is 0 :
                for z in range(0, 6) :
                    if i in ap[6][z] :
                        ap[6][z].remove(i)
                if snd is 1 :
                    if i in ap[6][8] :
                        ap[6][8].remove(i)
                elif snd is 2 :
                    if i in ap[6][7] :
                        ap[6][7].remove(i)
            elif fst is 1 :
                for z in range(0, 7) :
                    if i in ap[6][z] :
                        ap[6][z].remove(i)
            elif fst is 3 :
                for z in range(0, 6) :
                    if i in ap[7][z] :
                        ap[7][z].remove(i)
                if snd is 4 :
                    if i in ap[7][8] :
                        ap[7][8].remove(i)
                elif snd is 5 :
                    if i in ap[7][7] :
                        ap[7][7].remove(i)
            elif fst is 4 :
                for z in range(0, 7) :
                    if i in ap[7][z] :
                        ap[7][z].remove(i)
            elif fst is 6 :
                for z in range(0, 6) :
                    if i in ap[8][z] :
                        ap[8][z].remove(i)
                if snd is 7 :
                    if i in ap[8][8] :
                        ap[8][8].remove(i)
                elif snd is 8 :
                    if i in ap[8][7] :
                        ap[8][7].remove(i)
            elif fst is 7 :
                for z in range(0, 7) :
                    if i in ap[8][z] :
                        ap[8][z].remove(i)
    elif (fst, snd) in [(0, 3), (0, 6), (3, 6), (1, 4), (1, 7), (4, 7), (2, 5), (2, 8), (5, 8)] :  # row
        if b_num is 0 :
            if fst is 0 :
                if snd is 3 :
                    for z in range(2, 9) :
                        if i in ap[z][0] :
                            ap[z][0].remove(i)
                elif snd is 6 :
                    if i in ap[1][0] :
                        ap[1][0].remove(i)
                    for z in range(3, 9) :
                        if i in ap[z][0] :
                            ap[z][0].remove(i)
            elif fst is 3 :
                for z in range(3, 9) :
                    if i in ap[z][0] :
                        ap[z][0].remove(i)
            elif fst is 1 :
                if snd is 4 :
                    for z in range(2, 9) :
                        if i in ap[z][1] :
                            ap[z][1].remove(i)
                elif snd is 7 :
                    if i in ap[1][1] :
                        ap[1][1].remove(i)
                    for z in range(3, 9) :
                        if i in ap[z][1] :
                            ap[z][1].remove(i)
            elif fst is 4 :
                for z in range(3, 9) :
                    if i in ap[z][1] :
                        ap[z][1].remove(i)
            elif fst is 2 :
                if snd is 5 :
                    for z in range(2, 9) :
                        if i in ap[z][2] :
                            ap[z][2].remove(i)
                elif snd is 8 :
                    if i in ap[1][2] :
                        ap[1][2].remove(i)
                    for z in range(3, 9) :
                        if i in ap[z][2] :
                            ap[z][2].remove(i)
            elif fst is 5 :
                for z in range(3, 9) :
                    if i in ap[z][2] :
                        ap[z][2].remove(i)
        elif b_num is 1 :
            if fst is 0 :
                for z in range(0, 3) :
                    if i in ap[z][0] :
                        ap[z][0].remove(i)
                if snd is 3 :
                    for z in range(5, 9) :
                        if i in ap[z][0] :
                            ap[z][0].remove(i)
                elif snd is 6 :
                    if i in ap[4][0] :
                        ap[4][0].remove(i)
                    for z in range(6, 9) :
                        if i in ap[z][0] :
                            ap[z][0].remove(i)
            elif fst is 3 :
                for z in it.chain(range(0, 4), range(6, 9)) :
                    if i in ap[z][0] :
                        ap[z][0].remove(i)
            elif fst is 1 :
                for z in range(0, 3) :
                    if i in ap[z][1] :
                        ap[z][1].remove(i)
                if snd is 4 :
                    for z in range(5, 9) :
                        if i in ap[z][1] :
                            ap[z][1].remove(i)
                elif snd is 7 :
                    if i in ap[4][1] :
                        ap[4][1].remove(i)
                    for z in range(6, 9) :
                        if i in ap[z][1] :
                            ap[z][1].remove(i)
            elif fst is 4 :
                for z in it.chain(range(0, 4), range(6, 9)) :
                    if i in ap[z][1] :
                        ap[z][1].remove(i)
            elif fst is 2 :
                if snd is 5 :
                    for z in range(2, 9) :
                        if i in ap[z][2] :
                            ap[z][2].remove(i)
                elif snd is 8 :
                    if i in ap[4][2] :
                        ap[4][2].remove(i)
                    for z in range(3, 9) :
                        if i in ap[z][2] :
                            ap[z][2].remove(i)
            elif fst is 5 :
                for z in it.chain(range(0, 4), range(6, 9)) :
                    if i in ap[z][2] :
                        ap[z][2].remove(i)
        elif b_num is 2 :
            if fst is 0 :
                for z in range(0, 6) :
                    if i in ap[z][0] :
                        ap[z][0].remove(i)
                if snd is 3 :
                    if i in ap[8][0] :
                        ap[8][0].remove(i)
                elif snd is 6 :
                    if i in ap[7][0] :
                        ap[7][0].remove(i)
            elif fst is 3 :
                for z in range(0, 7) :
                    if i in ap[z][0] :
                        ap[z][0].remove(i)
            elif fst is 1 :
                for z in range(0, 6) :
                    if i in ap[z][1] :
                        ap[z][1].remove(i)
                if snd is 4 :
                    if i in ap[8][1] :
                        ap[8][1].remove(i)
                elif snd is 7 :
                    if i in ap[7][1] :
                        ap[7][1].remove(i)
            elif fst is 4 :
                for z in range(0, 7) :
                    if i in ap[z][1] :
                        ap[z][1].remove(i)
            elif fst is 2 :
                for z in range(0, 6) :
                    if i in ap[z][2] :
                        ap[z][2].remove(i)
                if snd is 5 :
                    if i in ap[8][2] :
                        ap[8][2].remove(i)
                elif snd is 8 :
                    if i in ap[7][2] :
                        ap[7][2].remove(i)
            elif fst is 5 :
                for z in range(0, 7) :
                    if i in ap[z][2] :
                        ap[z][2].remove(i)
        elif b_num is 3 :
            if fst is 0 :
                if snd is 3 :
                    for z in range(2, 9) :
                        if i in ap[z][3] :
                            ap[z][3].remove(i)
                elif snd is 6 :
                    if i in ap[1][3] :
                        ap[1][3].remove(i)
                    for z in range(3, 9) :
                        if i in ap[z][3] :
                            ap[z][3].remove(i)
            elif fst is 3 :
                for z in range(3, 9) :
                    if i in ap[z][3] :
                        ap[z][3].remove(i)
            elif fst is 1 :
                if snd is 4 :
                    for z in range(2, 9) :
                        if i in ap[z][4] :
                            ap[z][4].remove(i)
                elif snd is 7 :
                    if i in ap[1][4] :
                        ap[1][4].remove(i)
                    for z in range(3, 9) :
                        if i in ap[z][4] :
                            ap[z][4].remove(i)
            elif fst is 4 :
                for z in range(3, 9) :
                    if i in ap[z][4] :
                        ap[z][4].remove(i)
            elif fst is 2 :
                if snd is 5 :
                    for z in range(2, 9) :
                        if i in ap[z][5] :
                            ap[z][5].remove(i)
                elif snd is 8 :
                    if i in ap[1][5] :
                        ap[1][5].remove(i)
                    for z in range(3, 9) :
                        if i in ap[z][5] :
                            ap[z][5].remove(i)
            elif fst is 5 :
                for z in range(3, 9) :
                    if i in ap[z][5] :
                        ap[z][5].remove(i)
        elif b_num is 4 :
            if fst is 0 :
                for z in range(0, 3) :
                    if i in ap[z][3] :
                        ap[z][3].remove(i)
                if snd is 3 :
                    for z in range(5, 9) :
                        if i in ap[z][3] :
                            ap[z][3].remove(i)
                elif snd is 6 :
                    if i in ap[4][3] :
                        ap[4][3].remove(i)
                    for z in range(6, 9) :
                        if i in ap[z][3] :
                            ap[z][3].remove(i)
            elif fst is 3 :
                for z in it.chain(range(0, 4), range(6, 9)) :
                    if i in ap[z][3] :
                        ap[z][3].remove(i)
            elif fst is 1 :
                for z in range(0, 3) :
                    if i in ap[z][4] :
                        ap[z][4].remove(i)
                if snd is 4 :
                    for z in range(5, 9) :
                        if i in ap[z][4] :
                            ap[z][4].remove(i)
                elif snd is 7 :
                    if i in ap[4][4] :
                        ap[4][4].remove(i)
                    for z in range(6, 9) :
                        if i in ap[z][4] :
                            ap[z][4].remove(i)
            elif fst is 4 :
                for z in it.chain(range(0, 4), range(6, 9)) :
                    if i in ap[z][4] :
                        ap[z][4].remove(i)
            elif fst is 2 :
                for z in range(0, 3) :
                    if i in ap[z][5] :
                        ap[z][5].remove(i)
                if snd is 5 :
                    for z in range(5, 9) :
                        if i in ap[z][5] :
                            ap[z][5].remove(i)
                elif snd is 8 :
                    if i in ap[4][5] :
                        ap[4][5].remove(i)
                    for z in range(6, 9) :
                        if i in ap[z][5] :
                            ap[z][5].remove(i)
            elif fst is 5 :
                for z in it.chain(range(0, 4), range(6, 9)) :
                    if i in ap[z][5] :
                        ap[z][5].remove(i)
        elif b_num is 5 :
            if fst is 0 :
                for z in range(0, 6) :
                    if i in ap[z][3] :
                        ap[z][3].remove(i)
                if snd is 3 :
                    if i in ap[8][3] :
                        ap[8][3].remove(i)
                elif snd is 6 :
                    if i in ap[7][3] :
                        ap[7][3].remove(i)
            elif fst is 3 :
                for z in range(0, 7) :
                    if i in ap[z][3] :
                        ap[z][3].remove(i)
            elif fst is 1 :
                for z in range(0, 6) :
                    if i in ap[z][4] :
                        ap[z][4].remove(i)
                if snd is 4 :
                    if i in ap[8][4] :
                        ap[8][4].remove(i)
                elif snd is 7 :
                    if i in ap[7][4] :
                        ap[7][4].remove(i)
            elif fst is 4 :
                for z in range(0, 7) :
                    if i in ap[z][4] :
                        ap[z][4].remove(i)
            elif fst is 2 :
                for z in range(0, 6) :
                    if i in ap[z][5] :
                        ap[z][5].remove(i)
                if snd is 5 :
                    if i in ap[8][5] :
                        ap[8][5].remove(i)
                elif snd is 8 :
                    if i in ap[7][5] :
                        ap[7][5].remove(i)
            elif fst is 5 :
                for z in range(0, 7) :
                    if i in ap[z][5] :
                        ap[z][5].remove(i)
        elif b_num is 6 :
            if fst is 0 :
                if snd is 3 :
                    for z in range(2, 9) :
                        if i in ap[z][6] :
                            ap[z][6].remove(i)
                elif snd is 6 :
                    if i in ap[1][6] :
                        ap[1][6].remove(i)
                    for z in range(3, 9) :
                        if i in ap[z][6] :
                            ap[z][6].remove(i)
            elif fst is 3 :
                for z in range(3, 9) :
                    if i in ap[z][6] :
                        ap[z][6].remove(i)
            elif fst is 1 :
                if snd is 4 :
                    for z in range(2, 9) :
                        if i in ap[z][7] :
                            ap[z][7].remove(i)
                elif snd is 7 :
                    if i in ap[1][6] :
                        ap[1][6].remove(i)
                    for z in range(3, 9) :
                        if i in ap[z][7] :
                            ap[z][7].remove(i)
            elif fst is 4 :
                for z in range(3, 9) :
                    if i in ap[z][7] :
                        ap[z][7].remove(i)
            elif fst is 2 :
                if snd is 5 :
                    for z in range(2, 9) :
                        if i in ap[z][8] :
                            ap[z][8].remove(i)
                elif snd is 8 :
                    if i in ap[1][8] :
                        ap[1][8].remove(i)
                    for z in range(3, 9) :
                        if i in ap[z][8] :
                            ap[z][8].remove(i)
            elif fst is 5 :
                for z in range(3, 9) :
                    if i in ap[z][8] :
                        ap[z][8].remove(i)
        elif b_num is 7 :
            if fst is 0 :
                for z in range(0, 3) :
                    if i in ap[z][6] :
                        ap[z][6].remove(i)
                if snd is 3 :
                    for z in range(5, 9) :
                        if i in ap[z][6] :
                            ap[z][6].remove(i)
                elif snd is 6 :
                    if i in ap[4][6] :
                        ap[4][6].remove(i)
                    for z in range(6, 9) :
                        if i in ap[z][6] :
                            ap[z][6].remove(i)
            elif fst is 3 :
                for z in it.chain(range(0, 4), range(6, 9)) :
                    if i in ap[z][6] :
                        ap[z][6].remove(i)
            elif fst is 1 :
                for z in range(0, 3) :
                    if i in ap[z][7] :
                        ap[z][7].remove(i)
                if snd is 4 :
                    for z in range(5, 9) :
                        if i in ap[z][7] :
                            ap[z][7].remove(i)
                elif snd is 7 :
                    if i in ap[4][4] :
                        ap[4][4].remove(i)
                    for z in range(6, 9) :
                        if i in ap[z][7] :
                            ap[z][7].remove(i)
            elif fst is 4 :
                for z in it.chain(range(0, 4), range(6, 9)) :
                    if i in ap[z][7] :
                        ap[z][7].remove(i)
            elif fst is 2 :
                for z in range(0, 3) :
                    if i in ap[z][8] :
                        ap[z][8].remove(i)
                if snd is 5 :
                    for z in range(5, 9) :
                        if i in ap[z][8] :
                            ap[z][8].remove(i)
                elif snd is 8 :
                    if i in ap[4][8] :
                        ap[4][8].remove(i)
                    for z in range(6, 9) :
                        if i in ap[z][8] :
                            ap[z][8].remove(i)
            elif fst is 5 :
                for z in it.chain(range(0, 4), range(6, 9)) :
                    if i in ap[z][8] :
                        ap[z][8].remove(i)
        elif b_num is 8 :
            if fst is 0 :
                for z in range(0, 6) :
                    if i in ap[z][6] :
                        ap[z][6].remove(i)
                if snd is 3 :
                    if i in ap[8][6] :
                        ap[8][6].remove(i)
                elif snd is 6 :
                    if i in ap[7][6] :
                        ap[7][6].remove(i)
            elif fst is 3 :
                for z in range(0, 7) :
                    if i in ap[z][6] :
                        ap[z][6].remove(i)
            elif fst is 1 :
                for z in range(0, 6) :
                    if i in ap[z][7] :
                        ap[z][7].remove(i)
                if snd is 4 :
                    if i in ap[8][7] :
                        ap[8][7].remove(i)
                elif snd is 7 :
                    if i in ap[7][7] :
                        ap[7][7].remove(i)
            elif fst is 4 :
                for z in range(0, 7) :
                    if i in ap[z][7] :
                        ap[z][7].remove(i)
            elif fst is 2 :
                for z in range(0, 6) :
                    if i in ap[z][8] :
                        ap[z][8].remove(i)
                if snd is 5 :
                    if i in ap[8][8] :
                        ap[8][8].remove(i)
                elif snd is 8 :
                    if i in ap[7][8] :
                        ap[7][8].remove(i)
            elif fst is 5 :
                for z in range(0, 7) :
                    if i in ap[z][8] :
                        ap[z][8].remove(i)

def only_two_options(b_num, reduct):
    twos = []
    dupe = 0
    for j in range(9) :
        if len(reduct[j]) is 2 :
            if (reduct[j][0], reduct[j][1]) not in twos :
                twos.append((reduct[j][0], reduct[j][1]))
            else :
                dupe = (reduct[j][0], reduct[j][1])
                break
    if dupe != 0 :
        fst_pair = dupe[0]
        snd_pair = dupe[1]
        if b_num is 0 :
            for j in range(0, 3) :
                for k in range(0, 3) :
                    if len(ap[j][k]) is not 2 :
                        if fst_pair in ap[j][k] :
                            ap[j][k].remove(fst_pair)
                        if snd_pair in ap[j][k] :
                            ap[j][k].remove(snd_pair)
                    elif fst_pair not in ap[j][k] :
                        if snd_pair in ap[j][k] :
                            ap[j][k].remove(snd_pair)
                    elif snd_pair not in ap[j][k] :
                        if fst_pair in ap[j][k] :
                            ap[j][k].remove(fst_pair)
        elif b_num is 1 :
            for j in range(3, 6) :
                for k in range(0, 3) :
                    if len(ap[j][k]) is not 2 :
                        if fst_pair in ap[j][k] :
                            ap[j][k].remove(fst_pair)
                        if snd_pair in ap[j][k] :
                            ap[j][k].remove(snd_pair)
                    elif fst_pair not in ap[j][k] :
                        if snd_pair in ap[j][k] :
                            ap[j][k].remove(snd_pair)
                    elif snd_pair not in ap[j][k] :
                        if fst_pair in ap[j][k] :
                            ap[j][k].remove(fst_pair)
        elif b_num is 2 :
            for j in range(6, 9) :
                for k in range(0, 3) :
                    if len(ap[j][k]) is not 2 :
                        if fst_pair in ap[j][k] :
                            ap[j][k].remove(fst_pair)
                        if snd_pair in ap[j][k] :
                            ap[j][k].remove(snd_pair)
                    elif fst_pair not in ap[j][k] :
                        if snd_pair in ap[j][k] :
                            ap[j][k].remove(snd_pair)
                    elif snd_pair not in ap[j][k] :
                        if fst_pair in ap[j][k] :
                            ap[j][k].remove(fst_pair)
        elif b_num is 3 :
            for j in range(0, 3) :
                for k in range(3, 6) :
                    if len(ap[j][k]) is not 2 :
                        if fst_pair in ap[j][k] :
                            ap[j][k].remove(fst_pair)
                        if snd_pair in ap[j][k] :
                            ap[j][k].remove(snd_pair)
                    elif fst_pair not in ap[j][k] :
                        if snd_pair in ap[j][k] :
                            ap[j][k].remove(snd_pair)
                    elif snd_pair not in ap[j][k] :
                        if fst_pair in ap[j][k] :
                            ap[j][k].remove(fst_pair)
        elif b_num is 4 :
            for j in range(3, 6) :
                for k in range(3, 6) :
                    if len(ap[j][k]) is not 2 :
                        if fst_pair in ap[j][k] :
                            ap[j][k].remove(fst_pair)
                        if snd_pair in ap[j][k] :
                            ap[j][k].remove(snd_pair)
                    elif fst_pair not in ap[j][k] :
                        if snd_pair in ap[j][k] :
                            ap[j][k].remove(snd_pair)
                    elif snd_pair not in ap[j][k] :
                        if fst_pair in ap[j][k] :
                            ap[j][k].remove(fst_pair)
        elif b_num is 5 :
            for j in range(6, 9) :
                for k in range(3, 6) :
                    if len(ap[j][k]) is not 2 :
                        if fst_pair in ap[j][k] :
                            ap[j][k].remove(fst_pair)
                        if snd_pair in ap[j][k] :
                            ap[j][k].remove(snd_pair)
                    elif fst_pair not in ap[j][k] :
                        if snd_pair in ap[j][k] :
                            ap[j][k].remove(snd_pair)
                    elif snd_pair not in ap[j][k] :
                        if fst_pair in ap[j][k] :
                            ap[j][k].remove(fst_pair)
        elif b_num is 6 :
            for j in range(0, 3) :
                for k in range(6, 9) :
                    if len(ap[j][k]) is not 2 :
                        if fst_pair in ap[j][k] :
                            ap[j][k].remove(fst_pair)
                        if snd_pair in ap[j][k] :
                            ap[j][k].remove(snd_pair)
                    elif fst_pair not in ap[j][k] :
                        if snd_pair in ap[j][k] :
                            ap[j][k].remove(snd_pair)
                    elif snd_pair not in ap[j][k] :
                        if fst_pair in ap[j][k] :
                            ap[j][k].remove(fst_pair)
        elif b_num is 7 :
            for j in range(3, 6) :
                for k in range(6, 9) :
                    if len(ap[j][k]) is not 2 :
                        if fst_pair in ap[j][k] :
                            ap[j][k].remove(fst_pair)
                        if snd_pair in ap[j][k] :
                            ap[j][k].remove(snd_pair)
                    elif fst_pair not in ap[j][k] :
                        if snd_pair in ap[j][k] :
                            ap[j][k].remove(snd_pair)
                    elif snd_pair not in ap[j][k] :
                        if fst_pair in ap[j][k] :
                            ap[j][k].remove(fst_pair)
        elif b_num is 8 :
            for j in range(6, 9) :
                for k in range(6, 9) :
                    if len(ap[j][k]) is not 2 :
                        if fst_pair in ap[j][k] :
                            ap[j][k].remove(fst_pair)
                        if snd_pair in ap[j][k] :
                            ap[j][k].remove(snd_pair)
                    elif fst_pair not in ap[j][k] :
                        if snd_pair in ap[j][k] :
                            ap[j][k].remove(snd_pair)
                    elif snd_pair not in ap[j][k] :
                        if fst_pair in ap[j][k] :
                            ap[j][k].remove(fst_pair)

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
