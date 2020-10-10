from typing import List


class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
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

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        d = {}
        output = []
        for i, v in enumerate(nums):
            if target - v not in d:
                d[v] = i
            else:
                output.append(d[target - v])
                output.append(i)
                return output

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            ans = target - num
            if ans in dict:
                return [dict[ans], i]
            dict[nums[i]] = i
