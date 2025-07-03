class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        pointer = -1
        if len(s) == 1:
            return False
        for i in range(0, len(s)):
            if s[i] == '(':
                stack.append('(')
                flag = False
            if s[i] == ')':
                if stack and stack[pointer] == '(':
                    stack.pop()
                    flag = True
                else:
                    return False
            if s[i] == '{':
                stack.append('{')
                flag = False
            if s[i] == '}':
                if stack and stack[pointer] == '{':
                    stack.pop()
                    flag = True
                else:
                    return False
            if s[i] == '[':
                stack.append('[')
                flag = False
            if s[i] == ']':
                if stack and stack[pointer] == '[':
                    stack.pop()
                    flag = True
                else:
                    return False
        if stack: 
            return False
        else:
            return True
