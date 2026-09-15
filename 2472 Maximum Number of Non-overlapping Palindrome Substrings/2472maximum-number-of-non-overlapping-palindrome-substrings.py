class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        #cant think of an optimal solution, there is no constraint for length of string. an O(n^2) would surely lead to TLE. I was thinking of a two pointer approach, where two pointers at the starting position. find the difference between j and i, if it is greater than or equal to k - 1. then if check if it is a palindrome. if not then we shift j to the next position. now since j is at the next position we check if the lenght is greater than or equal to k. now checking if it is palindrome is the hardest part. we could do one thing that is, move both pointer towards each other, and if they reach at the same index without not missmatching we know we have a palindrome. if they dont match at any point we move on, but which pointer do we move forward?? oh yeah we move i to j, but what if theres a palindrome inside our substring. basically we have to find all possible substrings, which are greater than k and check if they are palindrome. 
        if len(s) < k:
            return 0

        #now we loop through the array, if element at index i == i + push or i == i + push + 1. then we check if substring, i to push or push + 1 respectively is a palindrome, and if it then we shitft i to push + 1 or push + 2 respectively. if not then we increment i, every time we encounter i we increment our count variable.

        def pal(string):
            if string == string[::-1]:
                return True
            return False

        count = 0
        i = 0
        while i <= len(s) - k:
            if pal(s[i:i + k]):
                count += 1
                i += k
            elif pal(s[i:i + k + 1]):
                count += 1
                i += k + 1
            else:
                i += 1
            
        return count
        

        