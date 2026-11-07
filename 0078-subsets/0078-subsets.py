class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res, visited = [[]], set()

        def dfs(i, arr):
            if i >= len(nums):
                return 
            
            arr.append(nums[i])
            res.append(arr.copy())
            dfs(i + 1, arr)

            arr.pop()
            dfs(i + 1, arr)

        dfs(0, [])

        return res
