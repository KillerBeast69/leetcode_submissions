class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        #it is not mentioned that the given array is sorted
        #find the number of 0 present in digits
        #also need to find out all the even gigits in given array
        c, e = 0, 0
        hashmap = {n:0 for n in digits}
        for n in digits:
            hashmap[n] += 1
            if n == 0:
                c += 1

            if n % 2 == 0:
                e += 1

        if e == 0:
            return 0

        #I should aim for O(n) algo
        #maybe not possible

        visited = set()
        count = 0

        def dfs(cur):
            nonlocal count
            tuplelist = tuple(cur) 
            if len(cur) == 3:
                if cur[2] % 2 == 0 and tuplelist not in visited:
                    count += 1
                visited.add(tuplelist)
                return
            
            for digit in hashmap:
                if hashmap[digit] > 0:
                    #but there is s problem here, what if there are repeated number?? do I need to maintain a hashmap??
                    #keeping track of how many numbers are left??
                    if len(cur) == 0 and digit == 0:
                        continue

                    
                    hashmap[digit] -= 1
                    cur.append(digit)

                    dfs(cur)

                    hashmap[digit] += 1    
                    cur.pop()
        dfs([])
        return count
        



