class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        #we have to use dfs? at each point, we have two options, either choose right block or the block below our current path. at each point we check if the char present at that block is either "(" or ")", if "(" we add one to the counter, and if the other, we decrement the counter. we maintain, index to know at which point we are at. basically find all the possible paths, from 0, 0. to m-1, n-1. where m and n are dimensions of the grid. when we reach at the bottom right most block, if the counter is 0, we return true, else false. at each point we have two choices, a and b, we return a or b. we could also use memoization. 
        m, n = len(grid), len(grid[0])
        if grid[0][0] == ")" or grid[m-1][n-1] == "(" or (m + n -1) % 2 != 0:
            return False

        memo = {}

        def dfs(i, j, count):
            if grid[i][j] == "(":
                count += 1
            if grid[i][j] == ")":
                count -= 1
    
            if count < 0:
                return False
            #we have to check for base case, and edge cases

            rem = (m - 1 - i) + (n - 1 - j)
            if count > rem:
                return False

            if i == m - 1 and j == n - 1:
                return count == 0

            if (i, j, count) in memo:
                return memo[(i, j, count)]

            #we have count, now what do we do??, check for edge cases?
            res = False
            if i + 1 < m:
                res = dfs(i + 1, j, count)
            if j + 1 < n:
                res = res or dfs(i, j + 1, count)
            
            memo[(i, j, count)] = res


            return res
        
        return dfs(0, 0, 0)