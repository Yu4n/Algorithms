# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/discuss/780199/JavaC%2B%2BPython-Straight-Forward-One-Pass

class Solution:
    def minInsertions(self, s):
        res = right = 0
        for c in s:
            if c == '(':
                if right % 2:
                    right -= 1
                    res += 1
                right += 2
            if c == ')':
                right -= 1
                if right < 0:
                    right += 2
                    res += 1
        return right + res
