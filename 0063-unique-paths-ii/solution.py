class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, columns = len(obstacleGrid), len(obstacleGrid[0])
        prevROW = [0] * columns
        for r in range(rows - 1, -1, -1):
            curROW = [0] * columns
            curROW[columns - 1] = 1
            for c in range(columns - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    curROW[c] = 0
                    continue
                elif (r == rows - 1) and (c == columns - 1):
                    curROW[c] = 1
                else:
                    right = curROW[c + 1] if c + 1 < columns else 0
                    down = prevROW[c] if r + 1 < rows else 0
                    curROW[c] = right + down
            prevROW = curROW
        return prevROW[0]

                
