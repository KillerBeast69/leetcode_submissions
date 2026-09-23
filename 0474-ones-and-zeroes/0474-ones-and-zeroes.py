class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:

        hashmap = {}

        def dfs(i, m, n):
            if i >= len(strs):
                return 0
            
            if (i, m, n) in hashmap:
                return hashmap[(i, m, n)]
            
            hashmap[(i, m, n)] = dfs(i + 1, m, n)
            c0, c1 = strs[i].count('0'), strs[i].count('1')
            if c0 <= m and c1 <= n:
                hashmap[(i, m, n)] = max(hashmap[(i, m, n)], 1 + dfs(i + 1, m - c0, n - c1))
            
            return hashmap[(i, m, n)]
        
        return dfs(0, m, n)
        