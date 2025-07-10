class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        l = 0
        r = m - 1
        while (l <= r):
            mid = (l + r) // 2
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][0] and target > matrix[mid][-1]:
                l = mid + 1
            else:
                break
        n = len(matrix[mid])
        l = 0
        r = n - 1
        c = mid
        while (l <= r):
            mid = (l + r) // 2
            if target < matrix[c][mid]:
                r = mid - 1
            elif target > matrix[c][mid]:
                l = mid + 1
            else:
                print(mid)
                return True
        print(mid)
        return False
