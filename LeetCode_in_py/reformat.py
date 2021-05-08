# https://leetcode.com/problems/reformat-the-string/
class Solution:
    def reformat(self, s: str) -> str:
        nums = ''.join(c for c in s if c.isnumeric())
        chars = ''.join(c for c in s if c.isalpha())
        s = ""
        if abs(len(nums) - len(chars)) > 1:
            return ""
        if len(nums) > len(chars):
            for num, char in zip(nums, chars):
                s += num
                s += char
            s += nums[-1]
            return s
        elif len(chars) > len(nums):
            for num, char in zip(nums, chars):
                s += char
                s += num
            s += chars[-1]
            return s
        else:
            for num, char in zip(nums, chars):
                s += num
                s += char
            return s
