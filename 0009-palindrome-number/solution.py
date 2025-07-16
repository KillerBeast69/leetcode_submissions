class Solution:
    def isPalindrome(self, x: int) -> bool:
        i = 0
        j = len(str(x)) - 1
        print(j)
        y = str(x)
        while(i <= j):
            if not y[i] == y[j]:
                return False
            i += 1
            j -= 1
        return True
        
