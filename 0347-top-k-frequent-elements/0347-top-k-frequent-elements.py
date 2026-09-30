class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        #best data structure I could think of is heap, a max heap, we just heapify the whole list and just pop k times. some edge cases like k cannot be greater than the lenght of the list. but if I had to implement this using hashing, cant think of anything. maybe lets say, we are iterating through the array, we increment its count in the hashmap, once we iterate through the array, we have all the uniquie elements and the count of how many times they have appeared, but the elements in the hashmap wont be sorted, so finding out the key, with the highest value would be O(n), where n is the number of uniquie elements in the array, and we need to find the key with the highest value k times, which can be len(hashmap) and m is the length of the array, therefore the total complexity would be O(n^2 + m) or O(n^2), what could I do to optimize it. or we could sort the list of pair ie the hashmap, in order of the value, and pop k times, sorting would be O(nlogn), here n is the len(hashmap), or number of unique elements, and iterating throught the array would be O(m) where m is the len of given array, therefore, the total time complexity would be O(nlogn) and space complexity would be O(n). omg we have to use bucket sort

        hashmap = {}
        bucket = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        for n, c in hashmap.items():
            bucket[c].append(n)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

        