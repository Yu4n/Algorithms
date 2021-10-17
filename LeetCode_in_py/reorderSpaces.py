class Solution:
    def reorderSpaces(self, text: str) -> str:
        space_count = text.count(' ')
        words = text.split()
        if len(words) == 1:
            return words[0] + ' ' * space_count
        spaces, tail = divmod(space_count, len(words) - 1)
        return (' ' * spaces).join(words) + ' ' * tail


sln = Solution()
print(sln.reorderSpaces("  hello"))
