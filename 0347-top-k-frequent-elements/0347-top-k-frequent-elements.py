class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] += 1
        
        bucket = [[] for i in range(len(nums) + 1)]
        for key, value in hashmap.items():
            bucket[value].append(key)

        res = []
        for array in reversed(bucket):
            for element in array:
                res.append(element)
                if len(res) == k:
                    return res
        
