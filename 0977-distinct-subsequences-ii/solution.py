class Solution:
    def distinctSubseqII(self, s: str) -> int:
        count = {}
        total = 1
        MOD = 10 ** 9 + 7
        for i in s:
            current_total = total
            total = 2 * total
            if i in count:
                total = total - count[i]
            count[i] = current_total 
                
        return (total - 1) % MOD
