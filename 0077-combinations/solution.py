class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        


        def helper(i, curcomb, combs, n, k):
            if len(curcomb) == k:
                combs.append(curcomb.copy())
                return
            
            if i > n:
                return

            for j in range(i, n + 1):
                curcomb.append(j)
                helper(j + 1, curcomb, combs, n, k)
                curcomb.pop()
        
        helper(1, [], combs, n, k)
        return combs
        
