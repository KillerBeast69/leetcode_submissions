class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        n = len(s)
        self.res = []
        
        @cache
        def dfs(i, string, d):
            if d < 0:
                return
            if i == n:
                if d == 0:
                    self.res.append(string)
                return
            if s[i] not in "()":
                dfs(i + 1, string + s[i], d)
            else:
                dfs(i + 1, string + s[i], d + (1 if s[i] == "(" else -1))
                dfs(i + 1, string, d)
        
        dfs(0, "", 0)
        maxl = max(len(st) for st in self.res)
        output = [st for st in self.res if len(st) == maxl]
        return output