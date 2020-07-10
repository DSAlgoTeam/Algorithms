'''
Assume there is a Land on top which a Builder decides to build a gated community. 
So he prepares an entire black/white schematic as to how this plot is to be built. 
This Black and White Image of the entire plot is fed to an Image Processing system. 

Let us assume that all of the dark area in this image corresponds to the parking area of this plot. 
If there are adjacent dark areas, it is still considered to be belonging to a single plot. 

Can you write a Polynomial Time algorithm for this Image processing system which indicates the 
number of parking lots and size of the largest parking lot ?
'''

def plot(matrix):
    '''
    black(0) and white(1) matrix

    prints the number of plots
    prints the largest plot size
    '''
    print(numParkingLots(matrix))
    print(largestPlotSize(matrix))

def numParkingLots(matrix):
    # considering black as 0 and white as 1
        if len(matrix) <1:
                return 0
        plots = 0
        size = 0
        plot_area = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 1:
                    plot_area.add((r,c))
        def dfs(r,c):
            if (r,c) in plot_area:
                plot_area.remove((r,c))
                return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
            return 0
        while plot_area:
            cell = plot_area.pop()
            plot_area.add(cell)
            
            size = max(size,dfs(cell[0],cell[1]))
            plots+=1
        return (plots,size)
                    

def largestPlotSize(matrix):
    # considering dark plots only
    '''
    largest square plot
    '''
    if(len(matrix) == 0) : return 0
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0 for i in range(cols+1)] for j in range(rows+1)]
    for i in range(1,rows+1):
        for j in range(1,cols+1):
            if matrix[i-1][j-1] == 1:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
                count = max(count,dp[i][j])
    return count