class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        #okay so I know we can hash a tuple, there may be different strings, but each type of anagram can be compared to one string, representing that anagram. for instance, we loop through the array, we check if that string is in hashmap, maybe with the use of tuple? so we hash, it and check if it is in the hashamap? but the thing is, lets say two strings are anagrams, they may not be literally the same, hashing them would lead to different results? soo what do we do? do we sort the array? and hash them and then compare them? like lets say we encounter the array, we sort it, hash it and compare it against the hashmap? each hashmap contains a list, once we hash we know which list we need to add on to. after everything is done, we generate a final array, where we start popping each list from the hashmap and append to the result array, but there is a problem, this is defi not optimal. sorting takes O(nlogn), lets say the max len of string is k and we would sort for each element of the given list, therefore the final time complexity would be O(nklogk) and space complexity would be O(n), ie the size of the hashmap.

        hashmap = {}
        for string in strs:
            element = "".join(sorted(string))
            if element not in hashmap:
                hashmap[element] = []
            hashmap[element].append(string)
        
        res = []
        for key in hashmap:
            res.append(hashmap[key])
        
        return res