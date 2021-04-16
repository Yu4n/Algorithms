class Solution:
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        l = 0
        r = m * n - 1
        while l != r:
            mid = (l + r) // 2
            if matrix[mid // m][mid % m] < target:
                l = mid + 1
            else:
                r = mid
        return matrix[r // m][r % m] == target
