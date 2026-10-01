class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        #the only solution I could think of is, having a hashmap. each index as key and value as 1 as default value. as we encounter number, we multiply each number with all the values of keys, except the current index, but that would be O(n^2), iterating throught the loop is O(n) and multiplying number at current index, with all the values of all keys is O(n) where n is the len of nums. the constraints for nums[i] are really small, how could that help? maybe have a hashmap, and count the number of occourances?? nvm we gonna use prefix and postfix

        pre = 1
        res = [1]
        for i in range(len(nums) - 1):
            pre *= nums[i]
            res.append(pre)
        
        post = 1
        for i in range(len(nums) - 1, 0, -1):
            post *= nums[i]
            res[i - 1] *= post
        
        return res

