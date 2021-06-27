class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        KEY = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        res = []
        if len(digits) == 1:
            i = len(KEY[digits[0]])
            for x in range(i):
                res.append(KEY[digits[0]][x])
        elif len(digits) == 2:
            i = len(KEY[digits[0]])
            j = len(KEY[digits[1]])
            for x in range(i):
                for y in range(j):
                    res.append(KEY[digits[0]][x] + KEY[digits[1]][y])
        elif len(digits) == 3:
            i = len(KEY[digits[0]])
            j = len(KEY[digits[1]])
            k = len(KEY[digits[2]])
            for x in range(i):
                for y in range(j):
                    for z in range(k):
                        res.append(KEY[digits[0]][x] + KEY[digits[1]][y] + KEY[digits[2]][z])
        elif len(digits) == 4:
            i = len(KEY[digits[0]])
            j = len(KEY[digits[1]])
            k = len(KEY[digits[2]])
            l = len(KEY[digits[3]])
            for x in range(i):
                for y in range(j):
                    for z in range(k):
                        for a in range(l):
                            res.append(KEY[digits[0]][x] + KEY[digits[1]][y] + KEY[digits[2]][z] + KEY[digits[3]][a])
        return res
