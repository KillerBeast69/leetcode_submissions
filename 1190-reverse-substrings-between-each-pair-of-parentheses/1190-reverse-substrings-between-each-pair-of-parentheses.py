class Solution:
    def reverseParentheses(self, s: str) -> str:
        pair = {}
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
            

        i, dir = 0, 1
        res = []
        while i < len(s):
            if s[i] == '(' or s[i] == ')':
                i = pair[i]
                dir = -dir
            else:
                res.append(s[i])
            i += dir
        
        return "".join(res)