class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_split = s.split()
        if len(pattern) != len(s_split):
            return False
        dc = {}
        for a, b in zip(pattern, s_split):
            if a not in dc.keys() and b not in dc.values():
                dc[a] = b
            elif (a not in dc.keys() and b in dc.values()) or dc[a] != b:
                return False
        return True
