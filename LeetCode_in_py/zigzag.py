class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lsOfString = [""] * numRows
        i = 0
        down = False
        for c in s:
            lsOfString[i] += c
            if down:
                i -= 1
                if i == 0:
                    down = False
            else:
                i += 1
                if i == numRows - 1:
                    down = True
        res = ""
        for ss in lsOfString:
            res += ss
        return res
