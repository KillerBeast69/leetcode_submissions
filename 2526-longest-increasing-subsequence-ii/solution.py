class SegmentTree:
    def __init__(self, N):
        self.n = N
        while (self.n & (self.n - 1)) != 0:
            self.n += 1
        self.tree = [0] * (2 * self.n)

    def update(self, i, val):
        if val <= self.tree[self.n + i]:
            return
        self.tree[self.n + i] = val
        j = (self.n + i) >> 1
        while j >= 1:
            self.tree[j] = max(self.tree[j << 1], self.tree[j << 1 | 1])
            j >>= 1

    def query(self, ql, qh):
        l = ql + self.n
        r = qh + self.n + 1
        res = 0
        while l < r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        ST = SegmentTree(max_val + 1)
        res = 0
        for num in nums:
            l = max(0, num - k)
            r = max(0, num - 1)
            curr = ST.query(l, r) + 1
            res = max(res, curr)
            ST.update(num, curr)

        return res
