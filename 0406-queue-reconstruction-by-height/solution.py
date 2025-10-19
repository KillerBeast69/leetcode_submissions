class BIT:
    def __init__(self, N):
        self.n = N + 1
        self.tree = [0] * self.n
        for i in range(self.n - 1):
            self.update(i, 1)

    def update(self, index, val):
        index += 1
        while index < self.n:
            self.tree[index] += val
            index += index & -index

    def getIdx(self, cnt, MSB):
        idx = 0
        while MSB:
            nxtIdx = idx + MSB
            if nxtIdx < self.n and cnt >= self.tree[nxtIdx]:
                idx = nxtIdx
                cnt -= self.tree[nxtIdx]
            MSB >>= 1
        return idx

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        people.sort(key=lambda x: (x[0], -x[1]))
        res = [[] for _ in range(n)]

        bit = BIT(n)
        MSB = 1 << int(math.log(n, 2))
        for p in people:
            idx = bit.getIdx(p[1], MSB)
            res[idx] = p
            bit.update(idx, -1)

        return res
