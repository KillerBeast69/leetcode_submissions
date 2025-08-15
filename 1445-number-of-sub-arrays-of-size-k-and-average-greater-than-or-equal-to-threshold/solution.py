class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        l = 0
        add = 0
        for r in range(len(arr)):
            if r - l + 1 > k:
                add -= arr[l]
                l += 1
            add += arr[r]
            print(r, add)
            if r - l + 1 == k and add / k >= threshold:
                res += 1
            r += 1
        return res 
