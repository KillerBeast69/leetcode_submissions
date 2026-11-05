class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        res = 0
        for i in arr1:
            dis = False
            for j in arr2:
                if abs(i-j) <= d:
                    dis = True
                    break
            if dis:
                res += 1


        return len(arr1) - res