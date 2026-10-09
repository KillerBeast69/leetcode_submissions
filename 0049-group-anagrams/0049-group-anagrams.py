class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for s in string:
                c = ord(s) - ord("a")
                count[c] += 1
            hashmap[tuple(count)].append(string)

        res = []
        for strings in hashmap.values():
            res.append(strings)
        
        return res