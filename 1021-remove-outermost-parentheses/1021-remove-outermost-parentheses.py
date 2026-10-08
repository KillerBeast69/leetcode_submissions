class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""

        stack = []
        d = 0
        for i in s:
            stack.append(i)
            if i == "(":
                d += 1
            else:
                d -= 1
                if d == 0:
                    res += "".join(stack[1:-1])
                    stack = []

        return res
        