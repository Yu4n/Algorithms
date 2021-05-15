# https://leetcode-cn.com/problems/longest-palindromic-substring/
class Solution:
    def centerExpand(self, s, left, right):
        while 0 <= left <= right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start = end = 0
        for i in range(len(s)):
            left1, right1 = self.centerExpand(s, i, i)
            print(left1, right1)
            left2, right2 = self.centerExpand(s, i, i + 1)
            print(left2, right2)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
            print(start, end)
            print()
        return s[start:end + 1]


x = Solution()
print(x.longestPalindrome("bb"))
