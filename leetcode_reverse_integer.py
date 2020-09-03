class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        y = abs(x)
        if 2 ** 31 - 1 < x or x < - 2 ** 31:
            return 0
        while y != 0:
            pop = y % 10
            y //= 10
            rev = rev * 10 + pop
        if 2 ** 31 - 1 < rev or rev < - 2 ** 31:
            return 0
        if x < 0:
            return -rev
        else:
            return rev

