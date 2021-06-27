class Solution:
    def letterCombinations(self, digits):
        if '' == digits:
            return []
        key = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = ['']
        for c in digits:
            tmp = []
            for y in res:
                for x in key[c]:
                    tmp.append(y + x)
            res = tmp
        return res
