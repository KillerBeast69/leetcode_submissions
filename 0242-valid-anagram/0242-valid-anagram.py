class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        if len(s) != len(t):
            return False
        
        for i in s:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] += 1
        
        for i in t:
            if i not in hashmap or hashmap[i] <= 0:
                return False
            hashmap[i] -= 1
        
        return True