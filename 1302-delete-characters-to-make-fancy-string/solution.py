class Solution:
    def makeFancyString(self, s: str) -> str:
        i = 0
        new = s[i]
        count = 0
        x = ""
        for i in range(len(s)):
            if s[i] == new:
                count += 1
                if count <= 2:
                    x = x + s[i]
                else:
                    continue
            else:
                new = s[i]
                x = x + s[i]
                count = 1
        return x
