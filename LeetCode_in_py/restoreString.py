class Solution:
    def restoreString(self, s: str, indices) -> str:
        dic = {}
        for i in range(len(s)):
            dic[indices[i]] = s[i]
        res = ""
        for i in range(len(s)):
            res += dic[i]
        return res
