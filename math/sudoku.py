#!/usr/bin/python3
import copy

FULL_SET = set(range(1, 10))

def show_cells(cells, title):
    print("==== {} ====".format(title.upper()))
    print()
    for y in range(9):
        print(' '.join(map(lambda n: str(n) if n > 0 else '-', cells[y])))
    print()

def str2num(sa):
    na = []
    for r in sa:
        na.append(list(map(int, r)))
    return na

def blk_id(y, x):
    return y // 3 * 3 + x // 3

def find_min_cell(cells):
    pos = None
    minlen = 9
    for y in range(9):
        for x in range(9):
            l = len(cells[y][x])
            if l < 1:
                continue
            if minlen > l:
                minlen = l
                pos = (x, y)
    return pos

def calc_free(nums):
    row_used = [[] for i in range(9)]
    col_used = [[] for i in range(9)]
    blk_used = [[] for i in range(9)]
    for y in range(9):
        for x in range(9):
            val = nums[y][x]
            row_used[y].append(val)
            col_used[x].append(val)
            blk_used[blk_id(y, x)].append(val)
    row_free = [[] for i in range(9)]
    col_free = [[] for i in range(9)]
    blk_free = [[] for i in range(9)]
    for i in range(9):
       row_free[i] = FULL_SET - set(row_used[i])
       col_free[i] = FULL_SET - set(col_used[i])
       blk_free[i] = FULL_SET - set(blk_used[i])
    #print(row_free, col_free, blk_free)
    return (row_free, col_free, blk_free)

def valid(nums):
    row_free, col_free, blk_free = calc_free(nums)
    #print(row_free, col_free, blk_free)
    for i in range(9):
        if len(row_free[i]) > 0:
            return False
        if len(col_free[i]) > 0:
            return False
        if len(blk_free[i]) > 0:
            return False
    return True

def solve(nums):
    row_free, col_free, blk_free = calc_free(nums)
    cells =  [[[] for i in range(9)] for j in range(9)]
    newfilled = 0
    unfilled = 0
    for y in range(9):
        for x in range(9):
            if nums[y][x] > 0:
                continue
            choices = list(row_free[y] & col_free[x] & blk_free[blk_id(y, x)])
            unfilled += 1
            cells[y][x] = choices
    #print("%d cells filled, %d remain" % (newfilled, unfilled))
    if unfilled == 0:
        if valid(nums):
            #print("Found solution")
            return nums
        else:
            #print("Found, but not valid")
            show_cells(nums, "Invalid")
            return None
    pos = find_min_cell(cells)
    if pos is None:
        #print("Not valid solution")
        return None
    posx, posy = pos
    cell = cells[posy][posx]
    #print("({}, {}) => {}".format(posx, posy, cell))
    for v in cell:
        a = copy.deepcopy(nums)
        a[posy][posx] = v
        s = solve(a)
        if s is not None:
            return s

def ui_solve(q):
    a = str2num(q)
    show_cells(a, "Question")
    s = solve(a)
    if s is None:
        print("No solution!")
    else:
        show_cells(s, "Solution")

def main():
    ui_solve(["530070000", "600195000", "098000060", "800060003", "400803001", "700020006",
        "060000280","000419005", "000080079"])

    ui_solve(["800000000", "003600000", "070090200", "050007000", "000045700", "000100030",
        "001000068", "008500010", "090000400"])

    ui_solve(["800000004", "003600000", "070090200", "050007000", "000045700", "000100030",
        "001000068", "008500010", "090000400"])

main()

