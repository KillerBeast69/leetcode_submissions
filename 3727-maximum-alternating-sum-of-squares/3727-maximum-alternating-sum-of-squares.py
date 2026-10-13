class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        arr = [a*a for a in nums]
        arr.sort()
        n = len(arr)
        return sum(arr[n // 2: n]) - sum(arr[0: n // 2])