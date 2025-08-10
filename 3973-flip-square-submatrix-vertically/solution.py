class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        a = x + (k - 1)
        b = y + (k - 1)
        while(x < a):
            temp = grid[x][y:b+1]
            grid[x][y:b+1] = grid[a][y:b+1]
            grid[a][y:b+1] = temp
            x += 1
            a -= 1
        return grid
