# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s):
        max_ = cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
                max_ = max(cnt, max_)
            elif c == ')':
                cnt -= 1
        return max_
