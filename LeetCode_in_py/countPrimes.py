class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        is_primes = [True] * n
        for i in range(2, int(n ** 0.5 + 1)):
            if is_primes[i]:
                is_primes[i * i:n:i] = [False] * len(is_primes[i * i:n:i])
        return sum(is_primes[2:])


sln = Solution()
print(sln.countPrimes(13))
