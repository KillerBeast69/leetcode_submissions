class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set()
        negDiag = set()

        count = 0


        def backtracking(r):

            if r == n:
                nonlocal count
                count += 1
                return 


            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                backtracking(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)         
        
        backtracking(0)
        return count
