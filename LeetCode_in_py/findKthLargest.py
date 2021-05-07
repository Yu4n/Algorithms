class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        return sorted(nums)[len(nums)-k]
