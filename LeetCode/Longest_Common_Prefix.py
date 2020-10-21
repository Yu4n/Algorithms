class Solution:
    def longestCommonPrefix(self, strs: []) -> str:  # Vertical scanning method
        if not strs or not len(strs):  # or not and
            return ''
        for i in range(0, len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                # i == len(strs[j]) means strs[0] is longer than strs[j].
                if i == len(strs[j]) or strs[j][i] != c:  # or not and
                    return strs[0][0:i]
        return strs[0]

    def longestCommonPrefix1(self, strs):
        if not strs:
            return ""
        # strs = ["flower", "flow", "flight"]
        # shortest = min(strs, key=len), in which shortest == flow as parameter is key=min.
        strs.sort()
        shortest = strs[0]  # shortest == flight
        for i, ch in enumerate(shortest):  # Use enumerate to index.
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

    def longestCommonPrefix2(self, strs: []) -> str:  # Horizontal scanning method
        n = len(strs)
        if n == 0:
            return ''
        prefix = strs[0]
        for a in strs[1:]:  # Start from the second string in the list.
            while a.find(prefix) != 0:  # Locate the prefix.
                prefix = prefix[:-1]  # Slice out the last character.
                if not prefix:
                    return ''
        return prefix


x = Solution()
strs = ["ab", "a", 'abc']
print(x.longestCommonPrefix(strs))
