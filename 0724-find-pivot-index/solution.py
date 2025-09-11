class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        size = len(nums)
        postfix = []
        prefix = []
        i, j, post, pre = 0, size - 1, 0, 0
        while i < size:
            post += nums[i]
            pre += nums[j]
            i += 1
            j -= 1
            postfix.append(post)
            prefix.append(pre)
        i = 0
        j = 0
        print(postfix)
        prefix.reverse()
        print(prefix)
        while i < size:
            if postfix[i] == prefix[j]:
                return i
            i += 1
            j += 1
        return -1       
