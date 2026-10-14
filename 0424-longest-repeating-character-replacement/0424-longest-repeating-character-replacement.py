class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        i = 0
        maxf = 0
        for j in range(len(s)):
            if s[j] not in count:
                count[s[j]] = 0
            
            count[s[j]] += 1
            maxf = max(maxf, count[s[j]])

            if (j - i + 1) - maxf > k:
                count[s[i]] -= 1
                i += 1

            res = max(res, j - i + 1)

        return res