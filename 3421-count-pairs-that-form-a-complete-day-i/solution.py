class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count = 0
        for i in range(0, len(hours) - 1):
            for j in range(1,len(hours)):
                if j>i:
                    if ((hours[i] + hours[j]) % 24 == 0):
                        count = count + 1
        return count
                
