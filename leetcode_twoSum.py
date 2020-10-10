from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        sum = 0
        res = []
        for i in range(0, n):
            for j in range(i + 1, n):
                sum = nums[i] + nums[j]
                if sum == target:
                    res.append(i)
                    res.append(j)
                    return res
