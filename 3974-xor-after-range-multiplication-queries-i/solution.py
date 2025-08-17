import math
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        xor = 0
        #print(queries)
        for i in range(len(queries)):
            idx = queries[i][0]
            for j in range(len(nums)):
                #print("idx", idx)
                while(idx <= queries[i][1]):
                    nums[idx] = (nums[idx] * queries[i][3]) % (pow(10, 9) + 7)
                    #print(nums[idx])
                    idx += queries[i][2]
        for a in range(len(nums)):
            xor = xor ^ nums[a]
        return xor
                
        
