class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        t = []
        for i in range(0,len(s)):
            if k>len(s):
                j = (i+k)%len(s)
                t.append(s[j])
            else:
                if (i+k)>len(s)-1:
                    p = i+k - len(s)
                    t.append(s[p])
                else:
                    t.append(s[i+k])
        return "".join(t)
