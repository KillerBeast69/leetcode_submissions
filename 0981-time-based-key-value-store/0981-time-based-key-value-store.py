class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        array = self.hashmap.get(key, [])

        l = 0
        r = len(array) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2
            if timestamp >= array[m][0]:
                res = array[m][1]
                l = m + 1
            else:
                r = m - 1
            
        
        #we did not found the element, therefore we return the latest element
        return res





# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)