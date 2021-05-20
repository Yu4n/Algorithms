class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = len(num1)  # assume n >= m
        m = len(num2)
        if n < m:
            num1, num2 = num2, num1
            n, m = m, n
        product = 0
        for i in range(1, m + 1):
            multiplier = int(num2[m - i])  # current character of num2
            sum_ = 0
            for j in range(0, n):  # multiply num1 by multiplier
                multiplicand = int(num1[n - j - 1])
                num = multiplicand * (10 ** j) * multiplier
                sum_ += num
            product += sum_ * (10 ** (i - 1))
        return str(product)
