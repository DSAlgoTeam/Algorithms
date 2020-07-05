'''
backtracking
'''
def _is_in_grid(n, x, y):
    '''
    checks if x and y are in the n*n grid
    '''
    if (x < 0) or (x > n-1) or (y < 0) or (y > n-1):
        return False
    return True

def _recur(n, grid, x, y, step, xlst, ylst):
    '''
    recursive function for knight_tour
    '''
    print(step, x, y)
    if step == n*n + 1:
        return True
    for i in range(8): # Number of possible states that can be changed.
        newx = x + xlst[i]
        newy = y + ylst[i]
        if _is_in_grid(n, newx, newy) and grid[newx][newy] == -1:
            grid[newx][newy] = step
            if _recur(n, grid, newx, newy, step+1, xlst, ylst):
                return True
            grid[newx][newy] = -1 # return to previous state, and check next solution
    return False

def knight_tour(n = 8, startx = 0, starty = 0):
    '''
    n: grid dimension
    startx: starting position of x (from 0 to n-1)
    starty: starting position of y (from o to n-1)
    '''
    if not isinstance(n,int):
        raise TypeError('n should be int')
    if not isinstance(startx,int):
        raise TypeError('n should be int')
    if not isinstance(starty,int):
        raise TypeError('n should be int')

    if (startx > n-1) or (starty > n-1):
        raise ValueError('Starting position should be in the grid')

    mat = [[-1 for i in range(n)] for j in range(n)]
    # THE FOLLOWING ARRANGEMENT OF THE COORDINATES MAKES THE EXECUTION EXCESSIVELY LONG.
    # xlst = [1, 1, -1, -1, 2, 2, -2, -2] # state changes possible in x
    # ylst = [2, -2, 2, -2, 1, -1, 1, -1] # corresponding state changes in y
    # To avoid that problem, place the coordinates in clockwise or counter clockwise direction
    xlst = [2, 1, -1, -2, -2, -1, 1, 2]
    ylst = [1, 2, 2, 1, -1, -2, -2, -1]
    mat[startx][starty] = 1
    if _recur(n, mat, startx, starty, 2, xlst, ylst):
        for i in range(n):
            for j in range(n):
                print(mat[i][j],end = "\t")
            print(" ")
    else:
        print('Tour not possible')