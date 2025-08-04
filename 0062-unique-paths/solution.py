class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevROW = [0] * m
        for r in range(n - 1, -1, -1):
            curROW = [0] * m
            curROW[m - 1] = 1
            for c in range(m - 2, -1, -1):
                curROW[c] = curROW[c + 1] + prevROW[c]
            prevROW = curROW
        return prevROW[0]

