class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        #I cannot think of an optimal solution here, the best I can think of is O(n^2), through iteration or recursive dfs, loop through the array, for each element we find the other part, and form a shadow pair. if any element is less than the current element or the first part of the shadow pair, we move to the next element. if there is an element greater than element at index i, we form a pair, ie we increment the count.

        def bs(val, arr):

            l = 0
            r = len(arr)

            while l < r:
                index = (l + r) // 2
                if arr[index] < val:
                    l = index + 1
                else:
                    r = index
            
            return l
            
        count = 0
        stack = []
        for n in nums:
            count += bs(n, stack)
            while stack and stack[-1] > n:
                stack.pop()
            stack.append(n)

        #no way there is an better solution than O(n^2), do we have to use memoization with recursion here? no wonder its a medium. cant even think of any specific algorithms
        return count
