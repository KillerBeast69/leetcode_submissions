class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        def parse(start):
            cur = {""}
            uni = set()
            i = start

            while i < len(expression):
                char = expression[i]
                
                if char == "{":
                    nest, i = parse(i + 1)
                    cur = {a + b for a in cur for b in nest}

                elif char == "}":
                    uni.update(cur)
                    return uni, i + 1

                elif char == ",":
                    uni.update(cur)
                    cur = {""}
                    i += 1

                else:
                    cur = {a + char for a in cur}
                    i += 1

            uni.update(cur)
            return uni, i

        final, _ = parse(0)
        return sorted(list(final))       