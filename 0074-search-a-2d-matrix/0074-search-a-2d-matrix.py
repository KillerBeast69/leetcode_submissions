class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        m = 0

        while l <= r:
            if (matrix[l][0] == target or
                matrix[l][-1] == target or
                matrix[r][0] == target or
                matrix[l][-1] == target):
                return True
            
            m = (l + r) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                break
            elif target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1
        
        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            if (matrix[m][l] == target or
                matrix[m][r] == target):
                return True
            
            mid = (l + r) // 2
            if matrix[m][mid] == target:
                return True
            elif target < matrix[m][mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return False