class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxlength = 0
        hashtable = set()
        for r in range(len(s)):
            if s[r] not in hashtable:
                hashtable.add(s[r])
                maxlength = max(maxlength, r - l + 1)
            else:
                while(s[r] in hashtable):
                    hashtable.remove(s[l])
                    l += 1
                hashtable.add(s[r])
        return maxlength
            

        
