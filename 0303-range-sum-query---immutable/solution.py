class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.postfix = []
        post = 0
        for i in range(len(self.nums)):
            post += self.nums[i]
            self.postfix.append(post)
        print(self.postfix)

    def sumRange(self, left: int, right: int) -> int:
        return self.postfix[right] - self.postfix[left - 1] if left > 0 else self.postfix[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
