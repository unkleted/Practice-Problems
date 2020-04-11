# Problem 96

# Su Doku solver
# By solving all fifty puzzles find the sum of the 3-digit numbers found in the 
# top left corner of each solution grid; for example, 483 is the 3-digit number 
# found in the top left corner of the solution gruid above.

import numpy as np
import time
start_time = time.time()

def is_possible(row, column, the_grid):
    """Returns the True if number can go in row and column"""
    possibles = [p for p in range(1,10)]
    # Check rows
    for r in the_grid[row]:
        if r in possibles:
            possibles.remove(r)
    # Check columns
    for c in range(len(the_grid)):
        if the_grid[c][column] in possibles:
            possibles.remove(the_grid[c][column])
    # Check box
    box_i = row % 3
    if box_i == 0:
        i_to_check = [row, row+1, row+2]
    elif box_i == 1:
        i_to_check = [row-1, row, row+1]
    elif box_i == 2:
        i_to_check = [row-2, row-1, row]
    else:
        print("How did you break this?")
    box_j = column % 3
    if box_j == 0:
        j_to_check = [column, column+1, column+2]
    elif box_j == 1:
        j_to_check = [column-1, column, column+1]
    elif box_j == 2:
        j_to_check = [column-2, column-1, column]
    else:
        print("How did you break this?")
    for i in i_to_check:
        for j in j_to_check:
            if the_grid[i][j] in possibles:
                possibles.remove(the_grid[i][j])
    return possibles


def solve(the_grid):
    """Brute force solves a sudoku puzzle"""
    global sum_first_three
    for x in range(len(the_grid)):
        for y in range(len(the_grid[x])):
            if the_grid[x][y] == 0:
                for n in is_possible(x,y,the_grid):
                    the_grid[x][y] = n
                    solve(the_grid)
                    the_grid[x][y] = 0
                return
    first_three = int(str(the_grid[0][0]) + str(the_grid[0][1]) + str(the_grid[0][2]))
    sum_first_three += first_three
    #print(np.matrix(the_grid))


def split(line):
    return [int(char) for char in line]
    #return list(line)


def get_grids(grid_file):
    with open(grid_file) as file_object:
        lines = file_object.readlines()
    for line in range(len(lines)):
        if 'Grid ' in lines[line]:
            grid = []
            tmp_grid = lines[line+1:line+10]
            for g in tmp_grid:
                grid.append(split(g.rstrip()))
            #print(grid)
            solve(grid)

# grid = [
    # [0,0,3,0,2,0,6,0,0],
    # [9,0,0,3,0,5,0,0,1],
    # [0,0,1,8,0,6,4,0,0],
    # [0,0,0,1,0,2,9,0,0],
    # [7,0,0,0,0,0,0,0,8],
    # [0,0,6,7,0,8,2,0,0],
    # [0,0,2,6,0,9,5,0,0],
    # [8,0,0,2,0,3,0,0,9],
    # [0,0,5,0,1,0,3,0,0]
# ]

sum_first_three = 0
get_grids('text files\p096_sudoku.txt')
print(sum_first_three)
print(time.time() - start_time)