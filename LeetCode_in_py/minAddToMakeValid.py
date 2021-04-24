# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
class Solution:
    def minAddToMakeValid(self, s):
        ans = bal = 0
        for c in s:
            bal += 2 if c == '(' else -1
            # Keep track of the balance of the string: number of '(''s minus number of ')''s.
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal


x = Solution()
S = "()))(("
print(x.minAddToMakeValid(S))
