class Solution:
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            for x in matrix[i]:
                if x == target:
                    return True
                elif x > target:
                    break
        return False
