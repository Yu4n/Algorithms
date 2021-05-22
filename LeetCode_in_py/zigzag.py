class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        strings = [""] * numRows
        i = 0
        down = False
        for c in s:
            strings[i] += c
            i += -1 if down else 1
            down = not down if i == 0 or i == numRows - 1 else down
        return "".join(strings)
