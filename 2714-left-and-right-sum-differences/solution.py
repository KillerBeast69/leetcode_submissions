class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(0, len(nums)):
            left = 0
            right = 0
            for l in range(0, i):
                left = left + nums[l]
            for r in range(i+1, len(nums)):
                right = right + nums[r]
            sum = abs(left - right)
            answer.append(sum)
        return answer
            
