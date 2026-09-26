class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        hashmap = {}

        def dfs(i, j):
            if i >= len(word1):
                return len(word2) - j
            
            if j >= len(word2):
                return len(word1) - i
            
            if (i, j) in hashmap:
                return hashmap[(i, j)]

            if word1[i] == word2[j]:
                hashmap[(i, j)] = dfs(i + 1, j + 1)
            else:
                hashmap[(i, j)] = min(
                    1 + dfs(i + 1, j),
                    1 + dfs(i, j + 1),
                    1 + dfs(i + 1, j + 1)
                )
            
            return hashmap[(i, j)]
        return dfs(0, 0)
