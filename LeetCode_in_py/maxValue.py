# https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/
class Solution:
    def maxValue(self, grid: [[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for i in range(1, m):
            grid[0][i] += grid[0][i - 1]
        for j in range(1, n):
            grid[j][0] += grid[j - 1][0]
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = max(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]
