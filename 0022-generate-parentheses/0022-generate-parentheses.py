class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def dfs(o, t, s):
            if t == n * 2:
                if o == 0:
                    res.append(s)
                return
            
            if o > 0:
                dfs(o - 1, t + 1, s + ")")     
            dfs(o + 1, t + 1, s + "(")
             
        dfs(0, 0, "") 
        return res