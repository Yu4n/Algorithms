class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = self.digitalRoot(num)
        return num

    def digitalRoot(self, num):
        sum_ = 0
        while num > 0:
            tmp = num % 10
            sum_ += tmp
            num //= 10
        return sum_
