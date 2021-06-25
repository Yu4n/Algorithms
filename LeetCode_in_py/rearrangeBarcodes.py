from collections import Counter


class Solution:
    def rearrangeBarcodes(self, barcodes: [int]) -> [int]:
        n = len(barcodes)
        num_freq = Counter(barcodes)
        num_freq = sorted(num_freq.items(), key=lambda x: -x[1])
        res = [0] * n
        i = 0
        for x, fx in num_freq:
            for _ in range(fx):
                if i >= n:
                    i = 1
                res[i] = x
                i += 2
        return res
