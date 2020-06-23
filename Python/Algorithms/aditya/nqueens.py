N= int(input())
board = [[0]*N for _ in range(N)]

def attack(i, j):
    for m in range(N):
        if board[i][m]==1 or board[m][j]==1:
            return True

    for m in range(N):
        for n in range(N):
            if (m+n==i+j) or (m-n==i-j):
                if board[m][n]==1:
                    return True
    return False

def nqueen(n):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):

            if (not(attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1

                if nqueen(n-1)==True:
                    return True
                board[i][j] = 0

    return False

nqueen(N)

for each in board:
    print (each)
