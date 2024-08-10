class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        n = len(nums)
        while (len(nums)>1):
            mx = max(nums)
            mn = min(nums)
            final = (mx+mn)/2
            averages.append(final)
            nums.remove(mx)
            nums.remove(mn)
        return min(averages) 


