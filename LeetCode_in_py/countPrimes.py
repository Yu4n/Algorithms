class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        is_primes = [True] * n
        non_primes = 0
        for i in range(2, int(n ** 0.5 + 1)):
            if is_primes[i]:
                for j in range(i * i, n, i):
                    if is_primes[j]:
                        is_primes[j] = False
                        print("j: " + str(j))
                        non_primes += 1
        print(is_primes)
        print(len(is_primes[2:-1]))
        print("non_primes is: " + str(non_primes))
        return n - 2 - non_primes


sln = Solution()
print(sln.countPrimes(13))
