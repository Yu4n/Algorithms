from collections import Counter


class Solution:
    def singleNumber(self, nums) -> int:
        c = Counter(nums)
        for i in c:
            if c[i] == 1:
                return i
