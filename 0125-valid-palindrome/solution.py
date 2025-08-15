class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ""
        for letter in range(len(s)):
            palindrome += s[letter].lower() if s[letter].isalnum() else ''
        print(palindrome)
        i = 0
        j = len(palindrome) - 1
        while(i < j):
            if palindrome[i] != palindrome[j]:
                return False
            i += 1
            j -= 1
        return True
            

        
