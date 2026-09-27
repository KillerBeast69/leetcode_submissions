class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        #not sure how to approach this solution? should I calculate all the possible subsequences or should I expand from each element in both directions? with either choosing element or not. 

        memo = {}

        def dfs(i, j):
            if i > j:
                return 0

            if i == j:
                return 1

            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == s[j]:
                memo[(i, j)] = 2 + dfs(i + 1, j - 1)
            else:
                memo[(i, j)] = max(dfs(i + 1, j), dfs(i, j - 1))

            return memo[(i, j)]
        
        return dfs(0, len(s) - 1)
        