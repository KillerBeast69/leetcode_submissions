class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        hashset = set()

        i, j = 0, 0
        maxl = 0
        n = len(s)
        l = 0

        while i <= j < n:
            if s[j] in hashset:
                i += 1
                j = i
                l = 1
                hashset = set()
                hashset.add(s[j])
            else:
                l += 1
                hashset.add(s[j])
                maxl = max(maxl, l)
            j += 1

        return maxl
            