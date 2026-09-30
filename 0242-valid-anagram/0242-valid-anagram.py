class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = {}
        for l in s:
            if l not in hashmap:
                hashmap[l] = 1
                continue
            hashmap[l] += 1

        for l in t:
            if l not in hashmap or hashmap[l] < 1:
                return False
            hashmap[l] -= 1
        return True
        