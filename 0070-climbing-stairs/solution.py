class Solution:
    def climbStairs(self, n: int) -> int:
        x = 1
        y = 1
        value = 1
        for i in range(1, n):
            z = y + x
            value = z
            x = y
            y = z
        return value
         
