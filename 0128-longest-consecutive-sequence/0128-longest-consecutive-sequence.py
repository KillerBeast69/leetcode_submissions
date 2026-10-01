class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        hashset = set(nums)

        cmax = 1
        for n in hashset:
            #we have to check if a number is a start of sequence, we do that by checking if n - 1 exists in the hashset, if we do find the start of the sequence, we use a while loop and loop until we find the end of the sequence, we calculate its sequence and compare against max sequence we have encountered. 
            if n - 1 not in hashset:
                #we found a start of a sequence
                i = n
                c = 0
                while i in hashset:
                    c += 1
                    i += 1
                #we went through the sequence and found the end, also the length of the sequence
                cmax = max(cmax, c)
        
        return cmax
            
        