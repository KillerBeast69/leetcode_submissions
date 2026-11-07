class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i, total, arr):
            if total == target:
                res.append(arr.copy())
                return
            
            if i == len(candidates) or total > target:
                return 
            
            

            arr.append(candidates[i])
            dfs(i, total + candidates[i], arr)
            arr.pop()
            dfs(i + 1, total, arr)

        dfs(0, 0, [])

        return res
