class Solution:
    def summaryRanges(self, nums: [int]) -> [str]:
        if not nums:
            return []
        res = []
        start, end = 0, 1
        while end < len(nums):
            if nums[end - 1] == nums[end] - 1:
                end += 1
            else:
                res.append(str(nums[start])) if start == end - 1 else res.append(
                    str(nums[start]) + "->" + str(nums[end - 1]))
                start = end
                end = start + 1
        res.append(str(nums[start])) if start == end - 1 else res.append(str(nums[start]) + "->" + str(nums[end - 1]))
        return res
