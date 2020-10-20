class Solution:
    def longestCommonPrefix_bad(self, strs: []) -> str:  # Time Limit Exceeded
        leng = len(strs)
        i = 0
        while True:
            for j in range(0, leng - 1):
                if i == 0 and strs[j][i] != strs[j + 1][i]:
                    return ''
            for j in range(0, leng - 1):
                if strs[j][i] != strs[j + 1][i]:
                    return strs[0][0:i]
            i += 1

    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs, key=len)  # key=min as parameter
        for i, ch in enumerate(shortest):  # Use enumerate to index.
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest


x = Solution()
strs = ["flower", "flow", "flight"]
print(x.longestCommonPrefix(strs))
