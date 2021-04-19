from collections import Counter


class Solution:
    def singleNumber(self, nums):
        dc = Counter(nums)
        res = []
        for d in dc:
            if dc[d] == 1:
                res.append(d)
        return res
