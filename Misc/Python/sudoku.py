'''
Solving sudoku using backtracking.
'''
import os
def _clear_screen():
    # to clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

# Random easy problem from the internet.
# 0 6 0 3 0 0 8 0 4
# 5 3 7 0 9 0 0 0 0
# 0 4 0 0 0 6 3 0 7
# 0 9 0 0 5 1 2 3 8
# 0 0 0 0 0 0 0 0 0
# 7 1 3 6 2 0 0 4 0
# 3 0 6 4 0 0 0 1 0
# 0 0 0 0 6 0 5 2 3
# 1 0 2 0 0 9 0 8 0

def _show(grid):
    for i in grid:
        for j in grid[0]:
            print(grid[i][j], end = " ")
        print(" ")


def sudoku():
    grid = [
        [0,6,0,3,0,0,8,0,4],
        [5,3,7,0,9,0,0,0,0],
        [0,4,0,0,0,6,3,0,7],
        [0,9,0,0,5,1,2,3,8],
        [0,0,0,0,0,0,0,0,0],
        [7,1,3,6,2,0,0,4,0],
        [3,0,6,4,0,0,0,1,0],
        [0,0,0,0,6,0,5,2,3],
        [1,0,2,0,0,9,0,8,0]
    ]
    bigmap = {
        '10': {},'20': {},'30': {},'40': {},'50': {},'60': {},'70': {},'80': {},'90': {}, #rows
        '01': {},'02': {},'03': {},'04': {},'05': {},'06': {},'07': {},'08': {},'09': {}, #cols
        '11': {}, '44': {}, '77':{} # squares
    }
    