class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        counter = 0
        iteration = min(a,b)
        for i in range(1, iteration + 1):
            if a % i == 0 and b % i == 0:
                counter = counter + 1
        return counter
