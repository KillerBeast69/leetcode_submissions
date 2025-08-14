class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashtable = set()
        l = 0
        for r in range(len(nums)):
            if r - l > k:
                hashtable.remove(nums[l])
                l += 1
            if nums[r] in hashtable:
                return True
            hashtable.add(nums[r])
        return False

