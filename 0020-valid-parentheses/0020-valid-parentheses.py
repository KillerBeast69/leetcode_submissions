class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stack = []
        for i in s:
            if i in hashmap:
                if not stack:
                    return False
                if stack.pop() != hashmap[i]:
                    return False
            else:
                stack.append(i)
        
        return not stack
