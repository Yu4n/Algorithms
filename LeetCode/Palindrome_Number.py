class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        digits = [int(n) for n in str(x)]
        length = len(digits)
        for i in range(0, length // 2 + 1):
            if digits[i] != digits[length - i - 1]:
                return False
        return True
