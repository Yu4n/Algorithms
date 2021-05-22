class Solution:
    def secondHighest(self, s: str) -> int:
        first = sec = -1
        for c in s:
            if c.isdigit():
                d = ord(c) - ord('0')
                if first < d:
                    sec, first = first, d
                elif sec < d < first:
                    sec = d
        return sec
