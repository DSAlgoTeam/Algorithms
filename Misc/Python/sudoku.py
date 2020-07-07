'''
Solving sudoku using backtracking.
'''
import os
from time import sleep
def _clear_screen():
    '''
    to clear the screen
    ''' 
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
    '''
    print the grid
    '''
    print('-------------------------------')
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end = " ")
        print(" ")
    print('-------------------------------')
def _find_next_empty(grid, pos):
    '''
    finds next empty cell

    returns row+col tuple
    '''
    row, col = pos[0], pos[1]
    while row < 9 and col < 9:
        if grid[row][col] == 0:
            return [row,col]
        if col < 8:
            col+=1
            continue
        else :
            col = 0
            row += 1

def _remove_from_big_map(bigmap, pos, n):
    '''
    removes `n` from `bigmap`
    '''
    row = str(pos[0]+1)+'0' # +1 added to match the bigmap's keys
    col = '0'+str(pos[1]+1)
    sq = str((pos[0]-pos[0]%3)+1)+str((pos[1]-pos[1]%3)+1)
    bigmap[row].remove(n)
    bigmap[col].remove(n)
    bigmap[sq].remove(n)

def _update_big_map(bigmap, pos, n):
    '''
    Adds a number `n` in a cell to bigmap
    '''
    row = str(pos[0]+1)+'0' # +1 added to match the bigmap's keys
    col = '0'+str(pos[1]+1)
    sq = str((pos[0]-pos[0]%3)+1)+str((pos[1]-pos[1]%3)+1)
    bigmap[row].add(n)
    bigmap[col].add(n)
    bigmap[sq].add(n)

def _is_safe(bigmap, pos,n):
    '''
    Checks if the number `n` will be safe if it were to be inserted at `pos`
    '''
    row = str(pos[0]+1)+'0' # +1 added to match the bigmap's keys
    col = '0'+str(pos[1]+1)
    sq = str((pos[0]-pos[0]%3)+1)+str((pos[1]-pos[1]%3)+1)
    if n in bigmap[row] or n in bigmap[col] or n in bigmap[sq]:
        return False
    return True

def _recurs(grid, bigmap, pos):
    '''
    recursion function for sudoku
    '''
    if pos is None:
        return True
    row,col = pos[0], pos[1]
    for i in range(1,10):
        if _is_safe(bigmap, pos, i):
            grid[row][col] = i
            _update_big_map(bigmap, pos, i)
            newpos = _find_next_empty(grid, pos)
            _show(grid)
            # sleep(0.1) # For visualization
            os.system('cls' if os.name=='nt' else 'clear')
            if _recurs(grid, bigmap, newpos):
                return True
            grid[row][col] = 0
            _remove_from_big_map(bigmap, pos, i)
    return False
def sudoku():
    '''
    Sudoku solver
    '''
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
    bigmap = { # used this large sized map to avoid loops. Takes O(1) space
        '10': set(),'20': set(),'30': set(),'40': set(),'50': set(),'60': set(),'70': set(),'80': set(),'90': set(), #rows
        '01': set(),'02': set(),'03': set(),'04': set(),'05': set(),'06': set(),'07': set(),'08': set(),'09': set(), #cols
        '11': set(),'44': set(),'77': set(),'14': set(),'17': set(),'41': set(),'47': set(),'71': set(),'74': set()  #squares
    }
    # one pass to read the problem and assign numbers
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                continue
            _update_big_map(bigmap, [i,j], grid[i][j])
    pos = _find_next_empty(grid,[0,0])
    if _recurs(grid, bigmap, pos):
        _show(grid)
    else:
        print('No solution found')
    
    