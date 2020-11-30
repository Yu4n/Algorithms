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

    def findDisappearedNumbers1(self, nums):
        if not nums:
            return []
        # Set operation
        return list(set(range(1, len(nums) + 1)) - set(nums))


x = Solution()
ls = [6, 7, 7, 5, 6, 1, 2]
print(x.findDisappearedNumbers(ls))
