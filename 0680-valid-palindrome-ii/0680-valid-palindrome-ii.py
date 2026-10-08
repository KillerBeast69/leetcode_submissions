class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def ispal(s):
            return s == s[::-1]
        
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return ispal(s[i + 1:j + 1]) or ispal(s[i:j])
            i += 1
            j -=1
        return True