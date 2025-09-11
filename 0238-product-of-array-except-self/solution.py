class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postmul = []
        premul = []
        post, pre = 1, 1
        i, j = 0, len(nums) - 1
        while(i < len(nums)):
            post *= nums[i]
            pre *= nums[j]
            postmul.append(post)
            premul.append(pre)
            i += 1
            j -= 1
        print(postmul)
        premul.reverse()
        print(premul)
        final = [None] * len(nums)
        pre, post = 1, 1
        for n in range(len(nums)):
            if n - 1 >= 0:
                post = postmul[n-1]
            else:
                post = 1
            if n + 1 < len(nums):
                pre = premul[n+1]
            else:
                pre = 1
            final[n] = post * pre
        return final
            

