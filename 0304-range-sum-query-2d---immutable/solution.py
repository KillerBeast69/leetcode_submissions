class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.postmat = [[0] * (COLS + 1) for i in range(ROWS + 1)]
        for i in range(ROWS):
            prefix = 0
            for j in range(COLS):
                prefix += matrix[i][j]
                above = self.postmat[i][j+1]
                self.postmat[i+1][j+1] = prefix + above
        print(self.postmat)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.postmat[row2+1][col2+1] - self.postmat[row2+1][col1] - self.postmat[row1][col2+1] + self.postmat[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
