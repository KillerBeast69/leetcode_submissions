class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0] * k
        cur = [0] * k
        for n in nums:
            temp = [0] * k
            for rem in range(k):
                if res[rem] > 0:
                    new_rem = (rem * n) % k
                    temp[new_rem] += cur[rem] 

            cur_rem = n % k
            temp[cur_rem] += 1

            #how do I update res?? do I loop through temp again??
            for i in range(k):
                res[i] += temp[i]
            cur = temp

        return res
