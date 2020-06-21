class N_Queen:
        
        def __init__(self, N = 3):
            self.count = 0
            self.N = N
            self.matrix = []
            for i in range(N): self.matrix.append([0 for i in range(N)])

        
        def n_Queen(self, row = 0):
            '''
            return number of possible solutions for given 'N' in N-Queen's problem
            '''
            if row == self.N: 
                self.count += 1
                print(self.matrix)
                return
            for i in range(self.N):
                if self.possible(row, i):
                    self.matrix [row][i] = 1
                    self.n_Queen(row+1)
                    self.matrix [row][i] = 0


        def possible(self, row, col) -> bool:
            '''
            check if a queen can be placed in the given cell{row, col}
            '''
            #check if queen is in the same col
            i = row - 1
            while i >= 0:
                if self.matrix[i][col]: return False
                i -= 1

            #check for left diagonal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if self.matrix[i][j]: return False
                i -= 1
                j -= 1
 
            #check for right diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < self.N:
                if self.matrix[i][j]: return False
                i -= 1
                j += 1

            return True