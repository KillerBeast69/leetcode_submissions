class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        hashmap = {}

        def dfs(i, j):
            #what is the base case? is it when j == len(t)?? 
            #increment i and j when both are equal, and increment only i when they are not equal, base case would be when either i or j == len or their respective array, when they are equal we return 1, if not then we return 0, we could either increment only i, when they are not equal and increment both i and j when they are equal, and calculate the sum of both subarray. and return, use memoization to store calculated value.
            
            if i >= len(s) or j >= len(t):
                if j >= len(t):
                    return 1
                
                if i >= len(s):
                    return 0
            
            if (i, j) in hashmap:
                return hashmap[(i, j)]
            
            if s[i] == t[j]:
                #increment both pointers and just i
                hashmap[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                #only increment i
                hashmap[(i, j)] = dfs(i + 1, j)
            
            return hashmap[(i, j)]
        
        return dfs(0, 0)
             
        