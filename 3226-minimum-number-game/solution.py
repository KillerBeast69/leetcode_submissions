class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        i = 0
        while nums != []:
            x = min(nums)
            nums.remove(x)
            y = min(nums)
            nums.remove(y)
            arr.append(y)
            arr.append(x)
            i = i + 1
        return arr
