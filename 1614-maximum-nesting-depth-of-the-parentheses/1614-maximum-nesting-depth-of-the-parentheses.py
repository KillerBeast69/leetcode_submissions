class Solution:
    def maxDepth(self, s: str) -> int:
        maxd = 0
        c = 0
        for i in s:
            if i == "(":
                c += 1
            elif i == ")":
                maxd = max(maxd, c)
                c -= 1
        
        return maxd
        