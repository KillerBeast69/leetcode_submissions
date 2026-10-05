class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = (
            "+",
            "-",
            "*",
            "/"
        )
        
        stack = []

        def cal(a, b, operator):
            if operator == "+":
                return a + b
            elif operator == "-":
                return a - b
            elif operator == "*":
                return a * b
            else:
                #what do we do when b == 0?
                return a / b

        
        total = 0
        for i in range(len(tokens)):
            if tokens[i] in operators:
                total = cal(int(stack[-2]), int(stack[-1]), tokens[i])
                stack.pop()
                stack.pop()
                stack.append(total)
            else:
                stack.append(tokens[i])

        return int(stack[0])