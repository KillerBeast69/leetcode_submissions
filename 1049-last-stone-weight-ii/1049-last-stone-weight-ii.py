class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        stones_total = sum(stones)
        target = ceil(stones_total) // 2

        hashmap = {}

        def dfs(i, total):
            if total >= target or i >= len(stones):
                return abs(total - (stones_total - total))

            if (i, total) in hashmap:
                return hashmap[(i, total)]

            hashmap[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))
            
            return hashmap[(i, total)]

        return dfs(0, 0)
        