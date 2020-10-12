class Solution:
    def fib(self, N: int) -> int:
        fibo = {0: 0, 1: 1}
        for k in range(2, N + 1):
            res = fibo[k - 1] + fibo[k - 2]
            fibo[k] = res
        return fibo[N]
