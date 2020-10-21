class Solution:
    def longestCommonPrefix(self, strs: []) -> str:  # Time Limit Exceeded
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


x = Solution()
strs = ["dog", "racecar", "car"]
print(x.longestCommonPrefix(strs))
