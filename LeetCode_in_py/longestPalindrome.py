# https://leetcode.com/problems/longest-palindrome/
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        res = 0
        odd = False
        for key in freq:
            if freq[key] % 2 == 0:
                res += freq[key]
            else:
                res += freq[key] - 1
                odd = True
        if odd:
            res += 1
        return res
