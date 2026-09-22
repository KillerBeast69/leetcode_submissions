class Node:
    def __init__(self, k):
        self.boxProduct = 1
        self.count = [0] * k

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        #cant think of anything
        n = len(nums)
        tree = [None] * (4 * n)



        def merge(left, right):
            if not left: return right
            if not right: return left

            parent = Node(k)
            parent.boxProduct = (left.boxProduct * right.boxProduct) % k
            
            for i in range(k):
                parent.count[i] = left.count[i]

            for i in range(k):
                if right.count[i] > 0:
                    rem = (left.boxProduct * i) % k
                    parent.count[rem] += right.count[i]
                
            return parent
    
        def build(index, start, end):
            if start == end:
                #when I hit the node leaf, how do I set them up?
                tree[index] = Node(k)
                val = nums[start] % k
                tree[index].boxProduct = val
                tree[index].count[val] += 1
                return
            
            mid = (start + end) // 2
            build(2 * index + 1, start, mid)
            build(2 * index + 2, mid + 1, end)

            tree[index] = merge(tree[2 * index + 1], tree[2 * index + 2])
            
            #I need to find its parent, and the parents other node, and call merge on both of them
            #how do I traverse??
            
        def update(index, start, end, idx, value):
            #again, how do I traverse?
            if start == end:
                tree[index] = Node(k)
                val = value % k
                tree[index].boxProduct = val
                tree[index].count[val] += 1

                nums[idx] = value
                return
            
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * index + 1, start, mid, idx, value)
            else:
                update(2 * index + 2, mid + 1, end, idx, value)
            
            tree[index] = merge(tree[2 * index + 1], tree[2 * index + 2])
        
        def query(index, start, end, query_start, query_end):
            #same thing, how do I traverse?    
            if query_start <= start and end <= query_end:
                return tree[index]
            
            mid = (start + end) // 2

            if query_end <= mid:
                return query(2 * index + 1, start, mid, query_start, query_end)

            elif query_start > mid:
                return query(2 * index + 2, mid + 1, end, query_start, query_end)
            
            else:
                left_res = query(2 * index + 1, start, mid, query_start, query_end)
                right_res = query(2 * index + 2, mid + 1, end, query_start, query_end)
                return merge(left_res, right_res)
            
        build(0, 0, n - 1)
        ans = []

        for index, value, si, xi in queries:
            update(0, 0, n - 1, index, value)

            res = query(0, 0, n-1, si, n - 1)

            ans.append(res.count[xi])

        return ans
        