class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        hashmap = {}

        def dfs(i, total):
            if i >= len(coins) or total > amount:
                return 0
        
            if total == amount:
                return 1
            
            if (i, total) in hashmap:
                return hashmap[(i, total)]
            
            count = dfs(i, total + coins[i]) + dfs(i + 1, total)

            hashmap[(i, total)] = count
            return count
        
        return dfs(0, 0)