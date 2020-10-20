class Solution:
    """ The Fibonacci numbers are defined by recurrence 3.22. Give an O(n)
        time dynamic-programming algorithm to compute the nth Fibonacci number.
        Draw the subproblem graph. How many vertices and edges are in the graph? (CLRS p.370)"""
    def fib(self, N: int) -> int:
        f = [0, 1]
        if N <= 1:
            return N
        for i in range(2, N + 1):
            r = f[i - 2] + f[i - 1]
            f.append(r)
        return f[-1]

    def fib1(self, n: int) -> int:
        a,b = 0,1
        if n==0 or n==1:
            return n
        for i in range(n):
            total = a + b
            b=a
            a= total
        return total
