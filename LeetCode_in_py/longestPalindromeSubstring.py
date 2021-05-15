# https://leetcode-cn.com/problems/longest-palindromic-substring/
class Solution:
    def centerExpand(self, s, left, right):
        while 0 <= left and right < len(s) and s[left] == s[right]:  # left is always smaller than right
            left -= 1
            right += 1
        return left + 1, right - 1  # add and decrease one

    def longestPalindrome(self, s: str) -> str:
        start = end = 0
        for i in range(len(s)):
            left1, right1 = self.centerExpand(s, i, i)
            left2, right2 = self.centerExpand(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end + 1]
