class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        dct = {}
        for s in strs:
            t = "".join(sorted(s))
            if t not in dct:
                dct[t] = [s]
            else:
                dct[t].append(s)
        return list(dct.values())
