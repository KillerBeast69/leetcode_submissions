class Solution:
    def countCommas(self, n: int) -> int:
        power = len(str(n)) - 1

        def rec(num, pow):
            if num < 1000:
                return 0
            sub = num - (10 ** pow) + 1
            rem = pow // 3
            return (sub * (rem)) + rec(num - sub, pow - 1) 

        return rec(n, power)

        
        
