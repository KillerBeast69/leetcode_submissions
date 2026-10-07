class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m] or nums[l] == target or nums[r] == target:
                return True

            if nums[l] < nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[l] > nums[m]:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                l += 1
        
        return False