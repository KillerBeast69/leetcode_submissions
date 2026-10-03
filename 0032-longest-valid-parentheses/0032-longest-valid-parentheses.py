class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = r = vmax = 0
        for i in s:
            if i == "(":
                l += 1
            else:
                r += 1
            
            if l == r:
                vmax = max(vmax, 2 * r)
            elif r > l:
                l, r = 0, 0

        l = r = 0
        for i in reversed(s):
            if i == "(":
                l += 1
            else:
                r += 1
            
            if l == r:
                vmax = max(vmax, 2 * l)
            elif l > r:
                l, r = 0, 0
        
        return vmax