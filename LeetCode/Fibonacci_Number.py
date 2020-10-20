class Solution:
    def fib(self, N: int) -> int:
        f = [0, 1]
        if N <= 1:
            return N
        for i in range(2, N + 1):
            r = f[i - 2] + f[i - 1]
            f.append(r)
        return f[-1]
