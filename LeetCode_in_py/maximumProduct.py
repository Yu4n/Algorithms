class Solution:
    def maximumProduct(self, nums) -> int:
        list.sort(nums)
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
