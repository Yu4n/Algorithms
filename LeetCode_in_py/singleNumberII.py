from collections import Counter


class Solution:
    def singleNumber(self, nums) -> int:
        c = Counter(nums)
        for i in c:
            if c[i] == 1:
                return i

    def singleNumberBit(self, nums):
        res = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1
            rem = count % 3
            if i == 31 and rem:
                res -= 1 << 31
            else:
                res |= rem * (1 << i)
        return res
