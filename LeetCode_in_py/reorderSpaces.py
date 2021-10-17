class Solution:
    def reorderSpaces(self, text: str) -> str:
        space_count = text.count(' ')
        words = text.split()
        if len(words) == 1:
            return words[0] + ' ' * space_count
        print(space_count)
        average_spaces = (space_count // (len(words) - 1)) * ' '
        tail_space = space_count % (len(words) - 1)
        print(tail_space)
        res = average_spaces.join(words)

        # for word in words:
        #     res += word + ' ' * average_spaces
        # res.strip()
        # print(res)
        res += tail_space * ' '
        return res


sln = Solution()
print(sln.reorderSpaces("  hello"))
