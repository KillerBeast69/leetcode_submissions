class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        a, b = 0, 0
        res = []
        for c in seq:
            #now we have to check which one got choosen, a or b? based on that we will either append 0 or 1 to res array respectively.
            if c == "(":
                if a <= b:
                    a += 1
                    res.append(0)
                else:
                    b += 1
                    res.append(1)
            else:
                if a >= b:
                    a -= 1
                    res.append(0)
                else:
                    b -= 1
                    res.append(1)

        return res
            
        