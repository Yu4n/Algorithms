class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        for i in range(n):
            m = abs(nums[i]) - 1
            nums[m] = -nums[m] if nums[m] > 0 else nums[m]
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i + 1)
        return res


x = Solution()
ls = [6, 7, 7, 5, 6, 1, 2]
print(x.findDisappearedNumbers(ls))
