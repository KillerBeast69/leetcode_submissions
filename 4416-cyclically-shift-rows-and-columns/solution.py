class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        arr = [[0] * n for _ in range(n)]
        for i, k in enumerate(rowShift):
            for j in range(n):
                new_j = (j - k + n) % n
                new_k = colShift[new_j]
                new_i = (i - new_k + n) % n
                arr[new_i][new_j] = grid[i][j]


        return arr
            
        
