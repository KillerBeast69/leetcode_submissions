class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        if s[0] in hashmap:
            return False

        for b in s:
            if b == "(" or b == "[" or b == "{":
                stack.append(b)
            
            else:
                if not stack or hashmap[b] != stack[-1]:
                    return False
                stack.pop()

        return True if not stack else False
        