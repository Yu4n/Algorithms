from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq = Counter(s)
        freq = sorted(freq.items(), key=lambda k: -k[1])
        if freq[0][1] >= n / 2 + 1:
            return ""
        res = [""] * n
        i = 0
        for x, fx in freq:  # iterate the sorted dictionary
            for _ in range(fx):  # loop fx times
                if i >= n:
                    i = 1  # go back to index 1
                res[i] = x
                i += 2
        return "".join(res)

    def reorganizeString1(self, s: str) -> str:
        length = len(s)
        if length < 2:
            return s

        counts = Counter(s)
        counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        # if counts[0][1] > (length + 1) // 2:
        #     return ""
        if (counts[0][1] > length // 2 + 1 and length % 2 == 1) or (
                counts[0][1] >= length // 2 + 1 and length % 2 == 0):
            return ""

        odd, even, half = 1, 0, length // 2
        res = [""] * length

        for c, count in counts:
            while 0 < count <= half and odd < length:
                res[odd] = c
                count -= 1
                odd += 2
            while count > 0 and even < length:
                res[even] = c
                count -= 1
                even += 2
        return "".join(res)
