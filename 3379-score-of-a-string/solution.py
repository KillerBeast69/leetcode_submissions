class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(0, len(s)):
            if i+1 == len(s):
                break
            score += abs(ord(s[i]) - ord(s[i+1]))
        return score
