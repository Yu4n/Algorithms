import collections


class Solution:
    def topKFrequent(self, words: [str], k: int) -> [str]:
        freq = collections.defaultdict(lambda: 0)
        for word in words:
            freq[word] += 1
        res = sorted(freq, key=lambda x: (-freq[x], x))[:k]
        return res
