class Solution:
    def checkValidString(self, s: str) -> bool:
        lmin, lmax = 0, 0
        for i in s:
            if i == "(":
                lmin += 1
                lmax += 1
            elif i == ")":
                lmin -= 1
                lmax -= 1
            else:
                lmin -= 1
                lmax += 1
            
            if lmax < 0:
                return False
            lmin = max(lmin, 0)
        
        return lmin == 0