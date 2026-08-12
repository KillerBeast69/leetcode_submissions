class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        tracker = defaultdict(int)
        maxi = 0
        i, j = 0, 0
        for j in range(len(nums)):
            tracker[nums[j]] += 1
            while tracker[nums[j]] > k:
                tracker[nums[i]] -= 1
                i += 1

            maxi = max(maxi, j - i + 1)
        return maxi
        
