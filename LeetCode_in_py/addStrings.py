class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        n = len(num1) - 1
        m = len(num2) - 1
        carry = 0
        while n >= 0 or m >= 0:
            char1 = ord(num1[n]) if n >= 0 else ord('0')
            char2 = ord(num2[m]) if m >= 0 else ord('0')
            num = char1 + char2 + carry
            if num >= 106:
                num -= 10
                res += chr(num - 48)
                carry = 1
            else:
                res += chr(num - 48)
                carry = 0
            n -= 1
            m -= 1
        if carry:
            res += "1"
        return res[::-1]
