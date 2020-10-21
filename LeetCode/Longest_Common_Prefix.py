class Solution:
    def longestCommonPrefix(self, strs: []) -> str:  # Vertical scanning method
        if not strs:  # or, not and
            return ''
        for i in range(0, len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                # i == len(strs[j]) means strs[0] is longer than strs[j].
                if i == len(strs[j]) or strs[j][i] != c:  # or, not and
                    return strs[0][0:i]
        return strs[0]

    def longestCommonPrefix1(self, strs):  # a pythonic method.
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

    def longestCommonPrefix3(self, strs):  # Divide and conquer.
        """
        :type strs: List[str]
        :rtype: str
        """
        if not len(strs):
            return ''
        return self.recurse(strs)

    def recurse(self, strs):
        if len(strs) == 1:
            return strs[0]
        mid = len(strs) // 2
        lcpLeft = self.recurse(strs[:mid])
        lcpRight = self.recurse(strs[mid:])

        return self.commonPrefix(lcpLeft, lcpRight)

    def commonPrefix(self, str1, str2):
        ret = str1[:min(len(str1), len(str2))]
        for i in range(len(ret)):
            if ret[i] != str2[i]:
                ret = ret[:i]
                break
        return ret

    def longestCommonPrefix4(self, strs):  # Binary search.
        """
        :type strs: List[str]
        :rtype: str
        """
        if not len(strs):
            return ''
        minLen = min([len(s) for  s in strs])
        low, high = 0, minLen
        while low <= high:
            mid = (low + high) // 2
            if self.isCommonPrefix(strs, mid):
                low = mid + 1
            else:
                high = mid -1
        return strs[0][:(low+high) // 2]

    def isCommonPrefix(self, strs, l):
        str1 = strs[0][:l]
        for s in strs[1:]:
            if not s.startswith(str1):
                return False
        return True


x = Solution()
strs = ["ab", "a", 'abc']
print(x.longestCommonPrefix(strs))
