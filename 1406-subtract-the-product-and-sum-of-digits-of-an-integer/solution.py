class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        add = 0
        while(n > 0):
            digit = n % 10
            mul = mul*(digit)
            add = add+digit
            n = n//10
        final = mul - add
        return final
